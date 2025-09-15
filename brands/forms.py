from django.forms import ModelForm

from .models import Brand


class BrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = ["name", "description"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        if Brand.objects.filter(name__iexact=name):
            self.add_error(
                "name", "Essa marca já foi registrada no base de dados."
            )
        return name
