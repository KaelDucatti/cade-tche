from django.db import models

from brands.models import Brand
from categories.models import Category


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500)
    description = models.TextField()
    serial_number = models.CharField(
        max_length=50, unique=True, blank=True, null=True
    )
    cost_price = models.DecimalField(max_digits=20, decimal_places=2)
    selling_price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    brand = models.ForeignKey(
        Brand, on_delete=models.PROTECT, related_name="products"
    )
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name="products"
    )

    def __str__(self):
        return f"{self.title} {self.brand}"

    class Meta:
        ordering = ["title"]
        verbose_name_plural = "Products"
