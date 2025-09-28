from django.contrib import messages
from django.db import transaction
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .forms import InflowForm
from .models import Inflow


class InflowListView(ListView):
    model = Inflow
    template_name = "inflows_list.html"
    context_object_name = "inflows"

    def get_queryset(self):
        queryset = super().get_queryset().select_related("product", "supplier")
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
