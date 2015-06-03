from django.db import models
from django.contrib.auth.models import User
from django.db.models.aggregates import Avg
from datetime import datetime

class Recette(models.Model):
    user = models.ForeignKey(User,default=1,editable=False)
    type = models.ForeignKey('Type', null=True)
    titre = models.CharField(max_length=100)
    cout = models.FloatField(null=True)
    difficulte = models.ForeignKey('Difficulte',default=1)
    temps_preparation = models.IntegerField(null=True)
    temps_cuisson = models.IntegerField(null=True)
    temps_repos = models.IntegerField(null=True)


    def calculateAvg(self):
        return Note.objects.filter(recette = self).aggregate(Avg('note'))

    moyenne_note = property(calculateAvg)

    def __str__(self):
        return self.titre




class Photo(models.Model):
    recette = models.ForeignKey('Recette',null=True,editable=False)
    image = models.ImageField(upload_to="photos_recettes", max_length=100)


class Ingredient(models.Model):
    recette = models.ForeignKey('Recette', null=True,editable=False)
    nom = models.CharField(max_length=100)
    quantite = models.CharField(max_length=100)


class Etape(models.Model):
    recette = models.ForeignKey('Recette', null=True, editable=False)
    detail = models.TextField()


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

CHOICES = [(i,i) for i in range(11)]

class Note(models.Model):
    recette = models.ForeignKey('Recette', blank=True, null=True)
    user = models.ForeignKey(User, blank=True, null=True)
    note = models.IntegerField(choices=CHOICES)

    def __str__(self):
        return '%s' % (self.note)


class Commentaire(models.Model):
    recette = models.ForeignKey('Recette', blank=True, null=True)
    user = models.ForeignKey(User, blank=True, null=True, default=1)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,default=datetime.now, blank=True, null=True)
