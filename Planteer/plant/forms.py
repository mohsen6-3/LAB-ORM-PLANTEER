from django import forms
from plant.models import Plant

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "about": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "used_for": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "category": forms.Select(attrs={"class": "form-control"}), 
            "is_edible": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "image": forms.ClearableFileInput(attrs={"class": "form-control-file"}),
        }