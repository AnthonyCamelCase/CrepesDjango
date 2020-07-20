from django import forms
from .models import Article, Contact

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        exclude =("slug","date")

class NouveauContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
