**Projet django site de recettes de cuisine**

Le thème est from scratch, ce n'est pas un thème simplement importé.
Ajout de bootstrap, fancybox et jquery

**Modèles :**

L'objet recette à 3 foreign key :
- pour le type (Plat,desset...)
- la difficulte (Facile,...)
- l'user

La recette contient 1 une plusieur ingrédient, photos, notes, commentaires et étapes.
Les objets note et commentaire ont une foreign key vers l'user.

**Installation :**

*Procédure pour le chargement des données initiales*
#python manage.py loaddata data

**Compte utilisateur :**

 1.  LOGIN : john  PASSWORD : john (utilisateur invité avec trois recettes)
 2.  LOGIN : admin ou valentin PASSWORD : admin ou valentin (superuser)

**BILAN**

Toutes les fonctionnalités sont réalisées, à quelques exceptions press:
- Sur la création d'une recette, nous n'avons pas fait le bouton javascript permettant d'ajouter de nouveaux éléments (Ingrédient, Photos, Etapes)
- TODO