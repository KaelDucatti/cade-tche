from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .forms import SupplierForm
from .models import Supplier


class SupplierListView(ListView):
    model = Supplier
    template_name = "suppliers_list.html"
    context_object_name = "suppliers"

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get("name")
        if search:
            queryset = queryset.filter(name__icontains=search)
        return queryset.order_by("name")


class SupplierDetailView(DetailView):
    model = Supplier
    template_name = "suppliers_detail.html"
    context_object_name = "supplier"


class SupplierDeleteView(DeleteView):
    model = Supplier
    template_name = "suppliers_delete.html"
    success_url = reverse_lazy("suppliers:list")


class SupplierCreateView(CreateView):
    model = Supplier
    template_name = "suppliers_form.html"
    success_url = reverse_lazy("suppliers:list")
    form_class = SupplierForm


class SupplierUpdateView(UpdateView):
    model = Supplier
    template_name = "suppliers_form.html"
    success_url = reverse_lazy("suppliers:list")
    form_class = SupplierForm
