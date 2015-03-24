from django.db import models


class Photo:
    recette = models.ForeignKey('Recette')

class Recette:
    titre = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    difficulte = models.CharField(max_length=100)
    cout = models.FloatField()
    photo =


    def __str__(self):
        return self.text
