from django.db import models


class Categories(models.Model):
    nom_cat = models.CharField(max_length=100)
    des = models.TextField(null = True, blank = True)

    def __str__(self):
        chaine = f"{self.nom_cat}"
        return chaine


    def dico(self):
        return {"nom_cat": self.nom_cat, "des": self.des}


class Produits(models.Model):
    nom_prod = models.CharField(max_length=100)
    date_per = models.DateField(blank=True, null = True)
    photo = models.ImageField(upload_to="produits_images",blank=True, null=True)
    marque = models.CharField(max_length=100)
    auteur = models.CharField(max_length=100)
    categories = models.ForeignKey("categories", on_delete=models.CASCADE, default=None)

    def __str__(self):
        chaine = f"{self.nom_prod} de la marque {self.marque} et qui périme le {self.date_per}."
        return chaine

    def dico(self):
        return {"nom_prod": self.nom_prod, "date_per": self.date_per, "photo": self.photo, "marque": self.marque, "auteur": self.auteur, "categories": self.categories}

class Clients(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    num_client = models.IntegerField(null= False, max_length=14)
    date_inscri = models.DateField(null = False)
    adresse = models.CharField(max_length=200)

    def __str__(self):
        chaine = f"{self.nom} {self.prenom} inscrit/e le {self.date_inscri} habitant à {self.adresse}. Numéro de téléphone : {self.num_client}"
        return chaine

    def dico(self):
        return {"nom": self.nom, "prenom": self.prenom, "num_client": self.num_client, "date_inscri": self.date_inscri, "adresse": self.adresse}

class Commandes(models.Model):
    num_commande = models.IntegerField(null= False)
    date = models.DateField(null = False)
    #client = clef étrangère

    def __str__(self):
        chaine = f"Commande n°{self.num_commande} à la date {self.date}"
        return chaine


    def dico(self):
        return {"num_commande": self.num_commande, "date": self.date}

#class Liste(models.Model):
#commande = clef étrangere
#produit et quantité = clef etrangere

