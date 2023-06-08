from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import CommandesForm
from . import models

def ajoutcommandes(request):
        form = CommandesForm()
        return render(request, "commande/ajout.html", {"form": form})

def traitementcommandes(request):
    lform = CommandesForm(request.POST)
    if lform.is_valid():
        Commandes = lform.save()
        return HttpResponseRedirect("/driveapp/indexcommandes")
    else :
        return render(request, "commande/ajout.html", {"form": lform})

def indexcommandes(request):
    liste = list(models.Commandes.objects.all())
    return render(request, "commande/index.html",{"liste": liste})

def affichecommandes(request, id):
    commandes = models.Commandes.objects.get(pk=id)
    return render(request, "commande/affiche.html", {"commandes": commandes})

def updatecommandes(request, id):
    commandes = models.Commandes.objects.get(pk=id)
    form = CommandesForm(commandes.dico())
    return render(request,"commande/update.html",{"form": form, "id": id})

def traitementupdatecommandes(request, id):
    lform = CommandesForm(request.POST)
    if lform.is_valid():
        Commandes = lform.save(commit=False)
        Commandes.id = id
        Commandes.save()
        return HttpResponseRedirect("/driveapp/indexcommandes")
    else:
        return render(request, "commande/update.html", {"form": lform, "id": id})

def deletecommandes(request, id):
    commandes = models.Commandes.objects.get(pk=id)
    commandes.delete()
    return HttpResponseRedirect("/driveapp/indexcommandes")
