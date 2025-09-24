from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from .forms import CategoryForm
from .models import Category


class CategoryListView(ListView):
    model = Category
    template_name = "categories_list.html"
    context_object_name = "categories"
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get("search")
        if search:
            queryset = queryset.filter(name__icontains=search)
        return queryset.order_by("name")


class CategoryDetailView(DetailView):
    model = Category
    template_name = "categories_detail.html"
    context_object_name = "category"


class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = "categories_form.html"
    success_url = reverse_lazy("categories:list")


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = "categories_form.html"
    success_url = reverse_lazy("categories:list")


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "categories_delete.html"
    success_url = reverse_lazy("categories:list")
