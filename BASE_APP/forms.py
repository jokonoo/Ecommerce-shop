from django import forms
from .models import News

class CreateNewsForm(forms.Form):
    news_title = forms.CharField(label='Title:', max_length=150)
    news_content = forms.CharField(label = 'Content')
