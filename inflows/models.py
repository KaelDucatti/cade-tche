from django.db import models

from products.models import Product
from suppliers.models import Supplier


class Inflow(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    supplier = models.ForeignKey(
        Supplier, on_delete=models.PROTECT, related_name="inflows"
    )
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="inflows"
    )

    def __str__(self):
        return f"{self.supplier.name} - {self.quantity}un"

    class Meta:
        ordering = ["-updated_at", "-created_at"]
        verbose_name_plural = "Inflows"
