from django.forms import ModelForm, NumberInput, Select, Textarea

from .models import Inflow


class InflowForm(ModelForm):
    class Meta:
        model = Inflow
        exclude = ["id", "created_at", "updated_at"]
        widgets = {
            "supplier": Select(attrs={"class": "form-control"}),
            "product": Select(attrs={"class": "form-control"}),
            "quantity": NumberInput(attrs={"class": "form-control"}),
            "description": Textarea(
                attrs={"class": "form-control", "rows": 3}
            ),
        }
        labels = {
            "supplier": "Fornecedor",
            "product": "Produto",
            "quantity": "quantidade",
            "description": "Descrição",
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get("quantity")
        if quantity <= 0:
            self.add_error(
                "quantity", "A quantidade não pode ser zero ou inferior."
            )
        return quantity
