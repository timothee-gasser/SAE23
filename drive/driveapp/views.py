from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ProduitsForm
from . import models

def ajout(request, id):
        form = ProduitsForm()
        return render(request, "produit/ajout.html", {"form": form, "id": id})

def traitement(request, id):
    categorie = models.Categories.objects.get(pk=id)
    lform = ProduitsForm(request.POST, request.FILES)
    if lform.is_valid():
        produits = lform.save(commit=False)
        produits.categories = categorie
        produits.categories_id = id
        produits.save()
        return HttpResponseRedirect("/driveapp/indexcategories/")
    else :
        return render(request, "produit/ajout.html", {"form": lform})

def index(request):
    return render(request, "index.html")

def pageproduits(request):
    liste = list(models.Produits.objects.all())
    return render(request, "produit/index.html",{"liste": liste})

def affiche(request, id):
    produits = models.Produits.objects.get(pk=id)
    return render(request, "produit/affiche.html", {"produits": produits})

def update(request, id):
    produits = models.Produits.objects.get(pk=id)
    form = ProduitsForm(produits.dico())
    return render(request,"produit/update.html",{"form": form, "id": id})

def traitementupdate(request, id):
    lform = ProduitsForm(request.POST)
    if lform.is_valid():
        Produits = lform.save(commit=False)
        Produits.id = id
        Produits.save()
        return HttpResponseRedirect("/driveapp/indexcategories/")
    else:
        return render(request, "produit/update.html", {"form": lform, "id": id})

def delete(request, id):
    produits = models.Produits.objects.get(pk=id)
    produits.delete()
    return HttpResponseRedirect("/driveapp/indexcategories/")
