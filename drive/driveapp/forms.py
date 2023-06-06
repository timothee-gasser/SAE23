from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class ProduitsForm(ModelForm):
    class Meta:
        model = models.Produits
        fields = ('nom_prod', 'date_per', 'photo', 'marque', 'auteur')
        labels = {
            'nom_prod' : _('Nom Produit'),
            'date_per' : _('Date Péremption') ,
            'photo' : _('Photo'),
            'marque' : _('Marque'),
            'auteur': _('Auteur'),

        }

class CategoriesForm(ModelForm):
    class Meta:
        model = models.Categories
        fields = ('nom_cat', 'des')
        labels = {
            'nom_cat' : _('Nom Catégorie'),
            'des' : _('Description') ,

        }