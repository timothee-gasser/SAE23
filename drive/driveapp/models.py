from django.db import models
from django.db import models


class Categories(models.Model):
    nom_cat = models.CharField(max_length=100)
    des = models.TextField(null = True, blank = True)


class Produits(models.Model):
    nom_prod = models.CharField(max_length=100)
    date_per = models.DateField(blank=True, null = True)
    photo = models.ImageField(upload_to="prod")
    marque = models.CharField(max_length=100)
    auteur = models.CharField(max_length=100)
    categorie = models.CharField(max_length=100)


class Clients(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Commandes(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Liste(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
# Create your models here.
