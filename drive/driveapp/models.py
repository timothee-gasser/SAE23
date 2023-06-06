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
    #catégorie = clef etrangere

    def dico(self):
        return {"nom_prod": self.nom_prod, "date_per": self.date_per, "photo": self.photo, "marque": self.marque, "auteur": self.auteur}

class Clients(models.Model):
    num_client = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    date_inscri = models.DateField(null = False)
    adresse = models.CharField(max_length=200)

class Commandes(models.Model):
    num_commande = models.IntegerField(null= False)
    date = models.DateField(null = False)
    #client = clef étrangère

#class Liste(models.Model):
#commande = clef étrangere
#produit et quantité = clef etrangere

