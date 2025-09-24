from django.forms import ModelForm, Textarea, TextInput

from .models import Brand


class BrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = ["name", "description"]
        widgets = {
            "name": TextInput({"class": "form-control"}),
            "description": Textarea({"class": "form-control", "rows": 3}),
        }
        labels = {"name": "Nome", "description": "Descrição"}

    def clean_name(self):
        name = self.cleaned_data.get("name")

        queryset = Brand.objects.filter(name__iexact=name)

        if self.instance.pk:
            queryset = queryset.exclude(pk=self.instance.pk)

        if queryset.exists():
            self.add_error(
                "name", "Essa marca já foi registrada no base de dados."
            )
        return name
