from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ClientsForm
from . import models

def ajoutclients(request):
        form = ClientsForm()
        return render(request, "client/ajout.html", {"form": form})

def traitementclients(request):
    lform = ClientsForm(request.POST)
    if lform.is_valid():
        Clients = lform.save()
        return HttpResponseRedirect("/driveapp/indexclients")
    else :
        return render(request, "client/ajout.html", {"form": lform})

def indexclients(request):
    liste = list(models.Clients.objects.all())
    return render(request, "client/index.html",{"liste": liste})

def afficheclients(request, id):
    clients = models.Clients.objects.get(pk=id)
    return render(request, "client/affiche.html", {"clients": clients})

def updateclients(request, id):
    clients = models.Clients.objects.get(pk=id)
    form = ClientsForm(clients.dico())
    return render(request,"client/update.html",{"form": form, "id": id})

def traitementupdateclients(request, id):
    lform = ClientsForm(request.POST)
    if lform.is_valid():
        Clients = lform.save(commit=False)
        Clients.id = id
        Clients.save()
        return HttpResponseRedirect("/driveapp/indexclients")
    else:
        return render(request, "client/update.html", {"form": lform, "id": id})

def deleteclients(request, id):
    clients = models.Clients.objects.get(pk=id)
    clients.delete()
    return HttpResponseRedirect("/driveapp/indexclients")
