from django.urls import path
from articles import views


app_name='articles'

urlpatterns = [
    path('flow/', views.flow_list_articles, name='flow_list_articles'),
    path('start/', views.start_list_articles, name='start_list_articles'),
    path('celero/', views.celero_list_articles, name='celero_list_articles'),
    path('novo_artigo/', views.create_article, name='create_article'),
]