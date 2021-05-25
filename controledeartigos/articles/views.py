from django.shortcuts import render, redirect
from articles.models import Article
from articles.forms import ArticleForm
from django.contrib import messages


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

def create_article(request):
    template_name = 'articles/create_article.html'
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.owner = request.user
            f.save()
            messages.success(request, 'Artigo adicionado com sucesso')
        messages.error(request, form.errors)
    else:
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)
            