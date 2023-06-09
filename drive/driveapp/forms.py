from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class ProduitsForm(ModelForm):
    class Meta:
        model = models.Produits
        fields = ('nom_prod', 'date_per', 'photo2', 'marque', 'prix', 'quantite', 'categories')
        labels = {
            'nom_prod' : _('Nom Produit'),
            'date_per' : _('Date Péremption') ,
            'photo2' : _('Photo'),
            'marque' : _('Marque'),
            'prix': _('Prix'),
            'quantite': _('Quantité'),
            'categories': _('Catégorie')


        }

class CategoriesForm(ModelForm):
    class Meta:
        model = models.Categories
        fields = ('nom_cat', 'des')
        labels = {
            'nom_cat' : _('Nom Catégorie'),
            'des' : _('Description') ,

        }

class CommandesForm(ModelForm):
    class Meta:
        model = models.Commandes
        fields = ('num_commande', 'date', 'clients', 'produit')
        labels = {
            'num_commande' : _('Numéro de commande'),
            'date' : _('Date de la commande') ,
            'clients' : _('Nom Client'),
            'produit' : _('Produit'),


        }

class ClientsForm(ModelForm):
    class Meta:
        model = models.Clients
        fields = ('nom', 'prenom', 'num_client', 'date_inscri', 'adresse')
        labels = {
            'nom' : _('Nom'),
            'prenom' : _('Prénom') ,
            'num_client': _('Numéro de téléphone'),
            'date_inscri': _("Date d'inscription"),
            'adresse': _('Adresse'),


        }