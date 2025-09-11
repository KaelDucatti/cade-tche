from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "description",
        "serial_number",
        "cost_price",
        "selling_price",
        "quantity",
        "created_at",
        "updated_at",
        "brand",
        "category",
    )
    search_fields = (
        "title",
        "serial_number",
        "cost_price",
        "selling_price",
        "brand_name",
        "category__name",
    )
