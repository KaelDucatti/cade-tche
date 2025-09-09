from django.db import models

from products.models import Product


class Outflow(models.Model):
    id = models.AutoField(primary_key=True)
    quantity = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="ouflows"
    )

    def __str__(self):
        return f"{self.product.title} - {self.quantity}un"

    class Meta:
        ordering = ["-updated_at"]
        verbose_name_plural = "Outflows"
