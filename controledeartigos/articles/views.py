from django.shortcuts import render, redirect, get_object_or_404
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

def edit_article(request, id):
    template_name = 'articles/edit_article.html'
    context = {}
    article = get_object_or_404(Article, article_id=id, is_deleted=False)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            if article.product == 'CE':
                return redirect('artigos:celero_list_articles')
            elif article.product == 'ST':
                return redirect('artigos:start_list_articles')
            elif article.product == 'FW':
                return redirect('artigos:flow_list_articles')
    else:
        form = ArticleForm(instance=article)
    context['form'] = form
    return render(request, template_name, context)
            
def delete_article(request, id):
    template_name = 'article/delete_article.html'
    article = get_object_or_404(Article, article_id=id, is_deleted=False)
    article.is_deleted = True
    article.save()
    if article.product == 'CE':
        return redirect('artigos:celero_list_articles')
    elif article.product == 'ST':
        return redirect('artigos:start_list_articles')
    elif article.product == 'FW':
        return redirect('artigos:flow_list_articles')

def list_deleted_articles(request):
    template_name = 'articles/list_deleted_articles.html'
    context = {}
    deleted_articles = Article.objects.filter(is_deleted=True)
    context['articles'] = deleted_articles
    return render(request, template_name, context)
    
def recuperate_article(request, id):
    template_name = 'article/delete_article.html'
    article = get_object_or_404(Article, article_id=id, is_deleted=True)
    article.is_deleted = False
    article.save()
    if article.product == 'CE':
        return redirect('artigos:celero_list_articles')
    elif article.product == 'ST':
        return redirect('artigos:start_list_articles')
    elif article.product == 'FW':
        return redirect('artigos:flow_list_articles')