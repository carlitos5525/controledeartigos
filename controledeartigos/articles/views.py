from django.shortcuts import render,HttpResponse


def list_articles(request):
    return render(request, 'base.html', {})