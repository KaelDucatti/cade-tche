from django.forms import ModelForm, Textarea, TextInput

from .models import Supplier


class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = ["name", "description"]
        widgets = {
            "name": TextInput({"class": "form-control"}),
            "description": Textarea({"class": "form-control"}),
        }

    def clean_name(self):
        name = self.cleaned_data.get("name")

        queryset = Supplier.objects.filter(name__iexact=name)

        if self.instance.pk:
            queryset = queryset.exclude(pk=self.instance.pk)

        if queryset.exists():
            self.add_error(
                "name", "Esse fornecedor já foi registrado na base de dados."
            )

        return name
