from django.contrib import admin

from .models import Outflow


@admin.register(Outflow)
class OutflowAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "quantity",
        "description",
        "created_at",
        "updated_at",
        "product",
    )
    search_fields = ("product__title",)
