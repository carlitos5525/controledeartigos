from django.shortcuts import render,HttpResponse
from articles.models import Article


def list_articles(request):
    template_name = 'articles/list_articles.html'
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, template_name, context)