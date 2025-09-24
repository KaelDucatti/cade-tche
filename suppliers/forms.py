from django.forms import ModelForm

from .models import Supplier


class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = ["name", "description"]

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
