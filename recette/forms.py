from django import forms
from .models import Recette, Etape, Ingredient , Note, Commentaire, Photo
from django.forms.models import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RecetteForm(forms.ModelForm):
    required_css_class = 'required'
    class Meta:
        model = Recette

class EtapeCustomForm(forms.ModelForm):
    required_css_class = 'required'
    detail = forms.CharField(required = True, widget=forms.Textarea(attrs={'cols': 40, 'rows': 2}))
    class Meta:
        model = Etape


IngredientFormset = inlineformset_factory(Recette, Ingredient)
EtapeFormset = inlineformset_factory(Recette, Etape,form=EtapeCustomForm)
ImageFormset = inlineformset_factory(Recette, Photo)


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['note']


class CommentaireForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'cols': 100, 'rows': 5}))
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