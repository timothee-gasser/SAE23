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
    photo2 = models.ImageField(upload_to="produits_images/",blank=True, null=True)
    marque = models.CharField(max_length=100)
    prix = models.CharField(max_length=100)
    quantite = models.IntegerField(default=0)
    categories = models.ForeignKey("Categories", on_delete=models.CASCADE, default=None, null=True)

    def __str__(self):
        chaine = f"{self.nom_prod} de la marque {self.marque} au prix de {self.prix}€. Quantité : {self.quantite}"
        return chaine

    def dico(self):
        return {"nom_prod": self.nom_prod, "date_per": self.date_per, "photo2": self.photo2, "marque": self.marque, "prix": self.prix, "quantite": self.quantite, "categories": self.categories}

class Clients(models.Model):
    nom = models.CharField(max_length=200)
    prenom = models.CharField(max_length=200)
    num_client = models.CharField(null= False, max_length=10)
    date_inscri = models.DateField(null = False)
    adresse = models.CharField(max_length=200)

    def __str__(self):
        chaine = f"{self.nom} {self.prenom}"
        return chaine

    def dico(self):
        return {"nom": self.nom, "prenom": self.prenom, "num_client": self.num_client, "date_inscri": self.date_inscri, "adresse": self.adresse}

class Commandes(models.Model):
    num_commande = models.IntegerField(null= False)
    produit = models.ForeignKey("Produits", on_delete=models.CASCADE, default=None)
    date = models.DateField(null = False)
    clients = models.ForeignKey("Clients", on_delete=models.CASCADE, default=None)


    def __str__(self):
        chaine = f"Commande n°{self.num_commande} à la date {self.date} effectuée par {self.clients}."
        return chaine


    def dico(self):
        return {"num_commande": self.num_commande, "date": self.date}

class Liste(models.Model):
    commande = models.ForeignKey(Commandes, on_delete=models.CASCADE)

    def __str__(self):
        chaine = f"Commande n°{self.commande}."
        return chaine


    def dico(self):
        return {"commande": self.commande}

