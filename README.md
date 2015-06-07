#Projet django site de recettes de cuisine

### Thème
Le thème a été realisé from scratch, utilisation de bootstrap, fancybox et jquery

###Modèles :

L'objet recette à 3 foreign key :
- pour le type (Plat,desset...)
- la difficulte (Facile,...)
- l'user

La recette contient 1 une plusieurs ingrédients, photos, notes, commentaires et étapes.
Les objets note et commentaire ont une foreign key vers l'user.

###Installation des données :

> python manage.py loaddata data

Contenu :
- 5 difficultés
- 4 types de recette
- Des utilisateurs, recettes, notes et commentaires

###Compte utilisateur :

 Les mot de passe des utilisateurs sont égaux aux identifiants
 Il y a 2 superuser :
 - Login : admin, mot de passe : admin
 - Login : valentin, mot de passe : valentin

#BILAN

Toutes les fonctionnalités sont réalisées, à quelques exceptions près:
- Sur la création d'une recette, nous n'avons pas fait le bouton javascript permettant d'ajouter de nouveaux éléments (Ingrédients, Photos, Etapes)
- La modification fontionne mais uniquement pour l'objet recette