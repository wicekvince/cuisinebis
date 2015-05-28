from django.db import models
from django.contrib.auth.models import User


class Photo(models.Model):
    recette = models.ForeignKey('Recette')
    image = models.ImageField(upload_to="photos_recettes", max_length=100)


class Ingredient(models.Model):
    recette = models.ForeignKey('Recette')
    nom = models.CharField(max_length=100)
    quantite = models.CharField(max_length=100)


class Etape(models.Model):
    recette = models.ForeignKey('Recette')
    detail = models.CharField(max_length=100)


class Type(models.Model):
    title = models.CharField(max_length=256)
    label = models.CharField(max_length=100,default='Label')
    detail = models.TextField()

    def __str__(self):
        return self.title


class Difficulte(models.Model):
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text


TYPE_CHOICES = (
    (1, 'Entrée'),
    (2, 'Plat'),
    (3, 'Déssert'),
    (4, 'Apéro'),
)

DIFF_CHOICES = (
    (1, 'Très acile'),
    (2, 'Facile'),
    (3, 'Moyenne'),
    (4, 'Difficile'),
    (5, 'Difficile')
)


class Recette(models.Model):
    user = models.ForeignKey(User)
    type = models.ForeignKey('Type')
    titre = models.CharField(max_length=100)
    cout = models.FloatField()
    difficulte = models.ForeignKey('Difficulte',default=1)
    temps_preparation = models.IntegerField()
    temps_cuisson = models.IntegerField()
    temps_repos = models.IntegerField()

    def __str__(self):
        return self.titre


class Note(models.Model):
    recette = models.ForeignKey('Recette')
    user = models.ForeignKey(User)
    note = models.IntegerField()


class Commentaire(models.Model):
    recette = models.ForeignKey('Recette')
    user = models.ForeignKey(User)
    message = models.TextField()
