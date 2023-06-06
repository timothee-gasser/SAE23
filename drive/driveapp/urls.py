from django.urls import path
from . import views, views_categories

urlpatterns = [
    path('', views.index, name='index'),
    path("ajout/", views.ajout),
    path("traitement/", views.traitement),
    path("affiche/<int:id>/", views.affiche),
    path("update/<int:id>/", views.update),
    path("traitementupdate/<int:id>/", views.traitementupdate),
    path("delete/<int:id>/", views.delete),
    #path pour catégories
    path('indexcategorie/', views_categories.indexcategorie),
    path("ajoutcategorie/", views_categories.ajoutcategorie),
    path("traitementcategorie/", views_categories.traitementcategorie),
    path("affichecategorie/<int:id>/", views_categories.affichecategorie),
    path("updatecategorie/<int:id>/", views_categories.updatecategorie),
    path("traitementupdatecategorie/<int:id>/", views_categories.traitementupdatecategorie),
    path("deletecategorie/<int:id>/", views_categories.deletecategorie),

]