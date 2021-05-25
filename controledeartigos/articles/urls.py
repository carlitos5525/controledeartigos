from django.urls import path
from articles import views


app_name='articles'

urlpatterns = [
    path('', views.list_articles, name='list_articles')
]