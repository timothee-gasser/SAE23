from django.urls import path
from . import views, views_categories, views_commandes, views_clients, views_liste

urlpatterns = [
    path('', views.index),
    path("driveapp/pageproduits/", views.pageproduits),
    path("driveapp/ajout/<int:id>/", views.ajout),
    path("driveapp/traitement/<int:id>/", views.traitement),
    path("driveapp/affiche/<int:id>/", views.affiche),
    path("driveapp/update/<int:id>/", views.update),
    path("driveapp/traitementupdate/<int:id>/", views.traitementupdate),
    path("driveapp/delete/<int:id>/", views.delete),
    #path pour catégories
    path('driveapp/indexcategories/', views_categories.indexcategories),
    path("driveapp/ajoutcategories/", views_categories.ajoutcategories),
    path("driveapp/traitementcategories/", views_categories.traitementcategories),
    path("driveapp/affichecategories/<int:id>/", views_categories.affichecategories),
    path("driveapp/updatecategories/<int:id>/", views_categories.updatecategories),
    path("driveapp/traitementupdatecategories/<int:id>/", views_categories.traitementupdatecategories),
    path("driveapp/deletecategories/<int:id>/", views_categories.deletecategories),
    #path pour commandes
    path('driveapp/indexcommandes/', views_commandes.indexcommandes),
    path("driveapp/ajoutcommandes/", views_commandes.ajoutcommandes),
    path("driveapp/traitementcommandes/", views_commandes.traitementcommandes),
    path("driveapp/affichecommandes/<int:id>/", views_commandes.affichecommandes),
    path("driveapp/updatecommandes/<int:id>/", views_commandes.updatecommandes),
    path("driveapp/traitementupdatecommandes/<int:id>/", views_commandes.traitementupdatecommandes),
    path("driveapp/deletecommandes/<int:id>/", views_commandes.deletecommandes),
    # path pour clients
    path('driveapp/indexclients/', views_clients.indexclients),
    path("driveapp/ajoutclients/", views_clients.ajoutclients),
    path("driveapp/traitementclients/", views_clients.traitementclients),
    path("driveapp/afficheclients/<int:id>/", views_clients.afficheclients),
    path("driveapp/updateclients/<int:id>/", views_clients.updateclients),
    path("driveapp/traitementupdateclients/<int:id>/", views_clients.traitementupdateclients),
    path("driveapp/deleteclients/<int:id>/", views_clients.deleteclients),
    # path pour liste
    path('driveapp/indexliste/', views_liste.indexliste),
    path("driveapp/afficheliste/<int:id>/", views_liste.afficheliste),
    path("driveapp/updateliste/<int:id>/", views_liste.updateliste),
    path("driveapp/traitementupdateliste/<int:id>/", views_liste.traitementupdateliste),
    path("driveapp/deleteliste/<int:id>/", views_liste.deleteliste),

]