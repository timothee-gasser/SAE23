from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class ProduitsForm(ModelForm):
    class Meta:
        model = models.Produits
        fields = ('nom_prod', 'date_per', 'photo', 'marque', 'auteur', 'categories')
        labels = {
            'nom_prod' : _('Nom Produit'),
            'date_per' : _('Date Péremption') ,
            'photo' : _('Photo'),
            'marque' : _('Marque'),
            'auteur': _('Auteur'),
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
        fields = ('num_commande', 'date')
        labels = {
            'num_commande' : _('Numéro de commande'),
            'date' : _('Date de la commande') ,

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