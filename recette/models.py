from django.db import models
from django.contrib.auth.models import User
from django.db.models.aggregates import Avg


class Photo(models.Model):
    recette = models.ForeignKey('Recette', blank=True, null=True)
    image = models.ImageField(upload_to="photos_recettes", max_length=100)


class Ingredient(models.Model):
    recette = models.ForeignKey('Recette', blank=True, null=True)
    nom = models.CharField(max_length=100)
    quantite = models.CharField(max_length=100)


class Etape(models.Model):
    recette = models.ForeignKey('Recette', blank=True, null=True)
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

class Recette(models.Model):
    user = models.ForeignKey(User,default=1)
    type = models.ForeignKey('Type')
    titre = models.CharField(max_length=100)
    cout = models.FloatField()
    difficulte = models.ForeignKey('Difficulte',default=1)
    temps_preparation = models.IntegerField()
    temps_cuisson = models.IntegerField()
    temps_repos = models.IntegerField()


    def calculateAvg(self):
        return Note.objects.filter(recette = self).aggregate(Avg('note'))

    moyenne_note = property(calculateAvg)

    def __str__(self):
        return self.titre


class Note(models.Model):
    recette = models.ForeignKey('Recette', blank=True, null=True)
    user = models.ForeignKey(User, blank=True, null=True)
    note = models.IntegerField(choices=CHOICES)

    def __str__(self):
        return '%s' % (self.note)


class Commentaire(models.Model):
    recette = models.ForeignKey('Recette', blank=True, null=True)
    user = models.ForeignKey(User, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True,default=None, blank=True, null=True)
