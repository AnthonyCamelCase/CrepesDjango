from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from datetime import datetime

def home(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return HttpResponse("""
        <h1>Bienvenue sur mon blog !</h1>
        <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>
    """)

def view_article(request, id_article):

    if id_article > 100:
        return redirect('afficher_article', id_article=42)

    return HttpResponse(f"Vous avez demandé l'article n° {id_article} !")

# views.py
def list_articles(request, year, month=1):
    return HttpResponse(f'Articles de l année {year} et du mois {month}')

def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})


def addition(request, nombre1, nombre2):
    total = nombre1 + nombre2

    # Retourne nombre1, nombre2 et la somme des deux au tpl
    return render(request, 'blog/addition.html', locals())

