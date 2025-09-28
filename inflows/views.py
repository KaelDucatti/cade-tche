from django.contrib import messages
from django.db import transaction
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .forms import InflowForm
from .models import Inflow


class InflowListView(ListView):
    model = Inflow
    template_name = "inflows_list.html"
    context_object_name = "inflows"

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get("search")
        if search:
            queryset = queryset.filter(
                Q(product__title__icontains=search)
                | Q(supplier__name__icontains=search)
            )
        return queryset


class InflowDetailView(DetailView):
    model = Inflow
    template_name = "inflows_detail.html"
    context_object_name = "inflow"


class InflowDeleteView(DeleteView):
    model = Inflow
    template_name = "inflows_delete.html"
    success_url = reverse_lazy("inflows:list")

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()

        with transaction.atomic():
            inflow = self.object
            product = inflow.product

            if product.quantity < inflow.quantity:
                messages.error(
                    request,
                    f"Não é possível excluir, estoque insuficiente!. "
                    f"Atual: {product.quantity}, Necessário: {inflow.quantity}",
                )
                return redirect(self.success_url)

            product.quantity -= inflow.quantity
            product.save()

            messages.success(
                request,
                f"Entrada removida! Estoque atual: {product.quantity}un.",
            )
        return super().delete(request, *args, **kwargs)


class InflowCreateView(CreateView):
    model = Inflow
    template_name = "inflows_form.html"
    success_url = reverse_lazy("inflows:list")
    form_class = InflowForm

    def form_valid(self, form):
        with transaction.atomic():
            inflow = form.save()

            product = inflow.product
            product.quantity += inflow.quantity
            product.save()

            messages.success(
                self.request,
                f"Entrada registrada! Estoque atual: {product.quantity}un.",
            )

        return super().form_valid(form)


class InflowUpdateView(UpdateView):
    model = Inflow
    template_name = "inflows_form.html"
    success_url = reverse_lazy("inflows:list")
    form_class = InflowForm

    def form_valid(self, form):
        with transaction.atomic():
            old_inflow = Inflow.objects.select_for_update().get(
                pk=self.object.pk
            )
            old_quantity = old_inflow.quantity

            inflow = form.save()
            new_quantity = inflow.quantity

            difference = new_quantity - old_quantity

            product = inflow.product
            product.quantity += difference
            product.save()

            messages.success(
                self.request,
                f"Atualização registrada! Estoque atual: {product.quantity}un.",
            )
        return super().form_valid(form)
