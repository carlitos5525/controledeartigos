from django import forms

from articles.models import Article

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        exclude = ('owner', 'is_deleted', 'last_updated')
