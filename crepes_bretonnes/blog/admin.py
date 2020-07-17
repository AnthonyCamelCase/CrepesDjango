from django.contrib import admin
from django.utils.text import Truncator
from .models import Article, Categorie

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("titre",'categorie','auteur', 'date', 'apercu_contenu')
    list_filter = ('auteur', 'categorie')
    date_hierarchy = 'date'
    ordering = ('date',)
    search_fields = ('titre', 'contenu')
    fields = ('titre', 'auteur', 'categorie', 'contenu')

    def apercu_contenu(self, article):
        """
        Retourne les 40 premiers caractères du contenu de l'article,
        suivi de points de suspension si le texte est plus long.
        """
        return Truncator(article.contenu).chars(40, truncate='...')

    # En-tête de notre colonne
    apercu_contenu.short_description = 'Aperçu du contenu'


admin.site.register(Article, ArticleAdmin)
admin.site.register(Categorie)