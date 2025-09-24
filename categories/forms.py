from django.forms import ModelForm, Textarea, TextInput

from .models import Category


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["id", "name", "description"]
        widgets = {
            "name": TextInput({"class": "form-control"}),
            "description": Textarea({"class": "form-control", "rows": 3}),
        }

    def clean_name(self):
        name = self.cleaned_data.get("name")

        queryset = Category.objects.filter(name__iexact=name)

        if self.instance.pk:
            queryset = queryset.exclude(pk=self.instance.pk)

        if queryset.exists():
            self.add_error(
                "name", "Essa categoria já foi registrada na base de dados."
            )

        return name
