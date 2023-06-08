from django.urls import path
from . import views, views_categories, views_commandes, views_clients

urlpatterns = [
    path('', views.index),
    path("ajout/<int:id>/", views.ajout),
    path("traitement/<int:id>/", views.traitement),
    path("affiche/<int:id>/", views.affiche),
    path("update/<int:id>/", views.update),
    path("traitementupdate/<int:id>/", views.traitementupdate),
    path("delete/<int:id>/", views.delete),
    #path pour catégories
    path('indexcategories/', views_categories.indexcategories),
    path("ajoutcategories/", views_categories.ajoutcategories),
    path("traitementcategories/", views_categories.traitementcategories),
    path("affichecategories/<int:id>/", views_categories.affichecategories),
    path("updatecategories/<int:id>/", views_categories.updatecategories),
    path("traitementupdatecategories/<int:id>/", views_categories.traitementupdatecategories),
    path("deletecategories/<int:id>/", views_categories.deletecategories),
    #path pour commandes
    path('indexcommandes/', views_commandes.indexcommandes),
    path("ajoutcommandes/", views_commandes.ajoutcommandes),
    path("traitementcommandes/", views_commandes.traitementcommandes),
    path("affichecommandes/<int:id>/", views_commandes.affichecommandes),
    path("updatecommandes/<int:id>/", views_commandes.updatecommandes),
    path("traitementupdatecommandes/<int:id>/", views_commandes.traitementupdatecommandes),
    path("deletecommandes/<int:id>/", views_commandes.deletecommandes),
    # path pour clients
    path('indexclients/', views_clients.indexclients),
    path("ajoutclients/", views_clients.ajoutclients),
    path("traitementclients/", views_clients.traitementclients),
    path("afficheclients/<int:id>/", views_clients.afficheclients),
    path("updateclients/<int:id>/", views_clients.updateclients),
    path("traitementupdateclients/<int:id>/", views_clients.traitementupdateclients),
    path("deleteclients/<int:id>/", views_clients.deleteclients),

]