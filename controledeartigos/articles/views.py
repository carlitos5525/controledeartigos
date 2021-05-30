from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from articles.models import Article
from articles.forms import ArticleForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User
from django.http import Http404



@login_required(login_url='/accounts/login')
def flow_list_articles(request):
    template_name = 'articles/list_articles.html'
    articles = Article.objects.filter(is_deleted=False, product='FW').order_by('last_updated')
    users = User.objects.all()
    if request.GET.get('date_start_with') and request.GET.get('date_end_with'):
            start_with = request.GET.get('date_start_with')
            end_with = request.GET.get('date_end_with')
            articles = articles.filter(last_updated__range=(start_with, end_with))
    if request.GET.get('usuario'):
        user_id = request.GET.get('usuario')
        user = get_object_or_404(User, id=user_id)
        articles = articles.filter(owner=user)    
    if request.GET.get('query'):
        query = request.GET.get('query')
        articles = articles.filter(name__icontains=query)
    if request.GET.get('pendente'):
        articles = articles.filter(Q(status='AF') | Q(status='AR'))
    if request.GET.get('realizado'):
        articles = articles.filter(Q(status='FF') | Q(status='AO'))
   
    context = {
        'articles': articles,
        'product': 'Flow',
        'users': users
    }
    return render(request, template_name, context)

@login_required(login_url='accounts/login')
def start_list_articles(request):
    template_name = 'articles/list_articles.html'
    articles = Article.objects.filter(is_deleted=False, product='ST').order_by('last_updated')
    users = User.objects.all()

    if request.GET.get('date_start_with') and request.GET.get('date_end_with'):
            start_with = request.GET.get('date_start_with')
            end_with = request.GET.get('date_end_with')
            articles = articles.filter(last_updated__range=(start_with, end_with))
    if request.GET.get('usuario'):
        user_id = request.GET.get('usuario')
        user = get_object_or_404(User, id=user_id)
        articles = articles.filter(owner=user)    
    if request.GET.get('query'):
        query = request.GET.get('query')
        articles = articles.filter(name__icontains=query)
    if request.GET.get('pendente'):
        articles = articles.filter(Q(status='AF') | Q(status='AR'))
    if request.GET.get('realizado'):
        articles = articles.filter(Q(status='FF') | Q(status='AO'))
    context = {
        'articles': articles,
        'product': 'Start',
        'users': users
    }
    return render(request, template_name, context)

@login_required(login_url='accounts/login')
def celero_list_articles(request):
    template_name = 'articles/list_articles.html'
    articles = Article.objects.filter(is_deleted=False, product='CE').order_by('last_updated')
    users = User.objects.all()
    if request.GET.get('date_start_with') and request.GET.get('date_end_with'):
            start_with = request.GET.get('date_start_with')
            end_with = request.GET.get('date_end_with')
            articles = articles.filter(last_updated__range=(start_with, end_with))
    if request.GET.get('usuario'):
        user_id = request.GET.get('usuario')
        user = get_object_or_404(User, id=user_id)
        articles = articles.filter(owner=user)    
    if request.GET.get('query'):
        query = request.GET.get('query')
        articles = articles.filter(name__icontains=query)
    if request.GET.get('pendente'):
        articles = articles.filter(Q(status='AF') | Q(status='AR'))
    if request.GET.get('realizado'):
        articles = articles.filter(Q(status='FF') | Q(status='AO'))
    context = {
        'articles': articles,
        'product': 'Celero',
        'users': users
    }
    return render(request, template_name, context)

@login_required(login_url='accounts/login')
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

@login_required(login_url='accounts/login')
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
            
@login_required(login_url='accounts/login')
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

@login_required(login_url='accounts/login')
def list_deleted_articles(request):
    template_name = 'articles/list_deleted_articles.html'
    context = {}
    deleted_articles = Article.objects.filter(is_deleted=True).order_by('last_updated')
    context['articles'] = deleted_articles
    return render(request, template_name, context)

@login_required(login_url='accounts/login')  
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

@login_required(login_url='accounts/login')
def get_user_pendent_articles(request):
    template_name = 'articles/user_articles.html'
    context = {}
    user = request.user
    articles = Article.objects.filter(Q(status='AR') | Q(status='AF'), owner=user).order_by('name')
    context['articles'] = articles
    return render(request, template_name, context)

@login_required(login_url='accounts/login/')
def change_article_to_done(request, article_id):
    template_name = 'articles/confirm_change_to_done.html'
    context = {}
    article = Article.objects.get(article_id=article_id)
    if article.status == 'AF':
        article.status = 'FF'
        article.save()
    elif article.status == 'AR':
        article.status = 'AO'
        article.save()
    if article.product == 'CE':
        return redirect('artigos:celero_list_articles')
    elif article.product == 'ST':
        return redirect('artigos:start_list_articles')
    elif article.product == 'FW':
        return redirect('artigos:flow_list_articles')
