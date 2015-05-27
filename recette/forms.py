from django import forms
from .models import Recette, Etape, Ingredient , Note, Commentaire
from django.forms.models import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RecetteForm(forms.ModelForm):
    class Meta:
        model = Recette


class EtapeForm(forms.ModelForm):
    class Meta:
        model = Etape

class IngredientForm(forms.ModelForm):

    class Meta:
        model = Ingredient

RecetteIngredientFormset = inlineformset_factory(Recette, Ingredient)


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['note']

class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['message']

class TestForm(forms.Form):
    nom = forms.CharField(max_length=100)
    prenom = forms.CharField(max_length=100,required='true')


class RegistrationForm(UserCreationForm):
    required_css_class = 'required'
    email = forms.EmailField(required = True)
    first_name = forms.CharField(required = True, label="Prénom")
    last_name = forms.CharField(required = True, label="Nom")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self,commit = True):
        user = super(RegistrationForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()

        return user