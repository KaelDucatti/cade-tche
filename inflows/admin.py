from django.contrib import admin

from .models import Inflow


@admin.register(Inflow)
class InflowAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "quantity",
        "description",
        "created_at",
        "updated_at",
        "supplier",
        "product",
    )
    search_fields = ("supplier__name", "product__title")
