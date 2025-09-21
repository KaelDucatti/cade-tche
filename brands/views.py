from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .forms import BrandForm
from .models import Brand


class BrandListView(ListView):
    model = Brand
    template_name = "brand_list.html"
    context_object_name = "brands"
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get("search")
        if search:
            queryset = queryset.filter(name__icontains=search)
        return queryset.order_by("name")


class BrandDetailView(DetailView):
    model = Brand
    template_name = "brand_detail.html"
    context_object_name = "brand"


class BrandCreateView(CreateView):
    model = Brand
    form_class = BrandForm
    template_name = "brand_form.html"
    success_url = reverse_lazy("brands:list")


class BrandUpdateView(UpdateView):
    model = Brand
    form_class = BrandForm
    template_name = "brand_form.html"
    success_url = reverse_lazy("brands:list")


class BrandDeleteView(DeleteView):
    model = Brand
    template_name = "brand_delete.html"
    success_url = reverse_lazy("brands:list")
