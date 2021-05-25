from django.shortcuts import render,HttpResponse
from articles.models import Article


def flow_list_articles(request):
    template_name = 'articles/list_articles.html'
    articles = Article.objects.filter(is_deleted=False, product='FW')
    context = {
        'articles': articles
    }
    return render(request, template_name, context)

def start_list_articles(request):
    template_name = 'articles/list_articles.html'
    articles = Article.objects.filter(is_deleted=False, product='ST')
    context = {
        'articles': articles
    }
    return render(request, template_name, context)

def celero_list_articles(request):
    template_name = 'articles/list_articles.html'
    articles = Article.objects.filter(is_deleted=False, product='CE')
    context = {
        'articles': articles
    }
    return render(request, template_name, context)