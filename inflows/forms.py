from django.forms import ModelForm

from .models import Inflow


class InflowForm(ModelForm):
    class Meta:
        model = Inflow
        exclude = ["id", "created_at", "updated_at"]

    def clean_quantity(self):
        quantity = self.cleaned_data.get("quantity")
        if quantity <= 0:
            self.add_error(
                "quantity", "A quantidade não pode ser zero ou inferior."
            )
        return quantity
