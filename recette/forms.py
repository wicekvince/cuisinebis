from django import forms
from .models import Recette, Etape, Ingredient
from django.forms.models import inlineformset_factory


class RecetteForm(forms.ModelForm):
    class Meta:
        model = Recette


class EtapeForm(forms.ModelForm):
    class Meta:
        model = Etape

class IngredientForm(forms.ModelForm):

    class Meta:
        model = Ingredient




class TestForm(forms.Form):
    nom = forms.CharField(max_length=100)
    prenom = forms.CharField(max_length=100,required='true')