from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import CommandesForm
from . import models

def indexliste(request):
    liste = list(models.Liste.objects.all())
    return render(request, "liste/index.html",{"liste": liste})

def afficheliste(request, id):
    liste = models.Commandes.objects.get(pk=id)
    return render(request, "liste/affiche.html", {"liste": liste})

def updateliste(request, id):
    commandes = models.Liste.objects.get(pk=id)
    form = CommandesForm(Liste.dico())
    return render(request,"commande/update.html",{"form": form, "id": id})

def traitementupdateliste(request, id):
    lform = CommandesForm(request.POST)
    if lform.is_valid():
        Commandes = lform.save(commit=False)
        Commandes.id = id
        Commandes.save()
        return HttpResponseRedirect("/driveapp/indexliste")
    else:
        return render(request, "commande/update.html", {"form": lform, "id": id})

def deleteliste(request, id):
    commandes = models.Commandes.objects.get(pk=id)
    commandes.delete()
    return HttpResponseRedirect("/driveapp/indexliste")
