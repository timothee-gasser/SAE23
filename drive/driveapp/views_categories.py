from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import CategoriesForm
from . import models

def ajoutcategorie(request):
        form = CategoriesForm()
        return render(request, "categorie/ajout.html", {"form": form})

def traitementcategorie(request):
    lform = CategoriesForm(request.POST)
    if lform.is_valid():
        Produits = lform.save()
        return HttpResponseRedirect("/driveapp/produit/index.html")
    else :
        return render(request, "categorie/ajout.html", {"form": lform})

def indexcategorie(request):
    liste = list(models.Categories.objects.all())
    return render(request, "categorie/index.html",{"liste": liste})

def affichecategorie(request, id):
    categories = models.Categories.objects.get(pk=id)
    return render(request, "categorie/affiche.html", {"categories": categories})

def updatecategorie(request, id):
    categories = models.Categories.objects.get(pk=id)
    form = CategoriesForm(categories.dico())
    return render(request,"categorie/update.html",{"form": form, "id": id})

def traitementupdatecategorie(request, id):
    lform = CategoriesForm(request.POST)
    if lform.is_valid():
        Categories = lform.save(commit=False)
        Categories.id = id
        Categories.save()
        return HttpResponseRedirect("/driveapp/produit/index.html")
    else:
        return render(request, "categorie/update.html", {"form": lform, "id": id})

def deletecategorie(request, id):
    categories = models.Categories.objects.get(pk=id)
    categories.delete()
    return HttpResponseRedirect("/driveapp/produit/index.html")
