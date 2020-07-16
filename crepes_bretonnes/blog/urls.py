from django.urls import path
from . import views

urlpatterns = [
    path('accueil', views.home),
    path('article/<id_article>', views.view_article, name="afficher_article"),
    path('articles/<int:year>/', views.list_articles),
    path('articles/<int:year>/<int:month>', views.list_articles),
    path('date', views.date_actuelle),
    path('addition/<int:nombre1>/<int:nombre2>/', views.addition)
]

