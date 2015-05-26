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



TYPE_CHOICES = (
    (1, 'Entrée'),
    (2, 'Plat'),
    (3, 'Déssert'),
    (4, 'Apéro'),
)

DIFF_CHOICES = (
    (1, 'Recette Facile'),
    (2, 'Difficulté moyenne'),
    (3, 'Recette difficile'),
)


class Recette(models.Model):
    user = models.ForeignKey(User)
    titre = models.CharField(max_length=100)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES)
    difficulte = models.CharField(max_length=100, choices=DIFF_CHOICES)
    cout = models.FloatField()
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
