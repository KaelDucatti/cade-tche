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

    def clean_name(self):
        name = self.cleaned_data["name"]
        if Brand.objects.filter(name__iexact=name):
            self.add_error(
                "name", "Essa marca já foi registrada no base de dados."
            )
        return name
