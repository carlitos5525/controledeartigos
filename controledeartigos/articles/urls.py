from django.urls import path
from articles import views


app_name='articles'

urlpatterns = [
    path('flow/', views.flow_list_articles, name='flow_list_articles'),
    path('start/', views.start_list_articles, name='start_list_articles'),
    path('celero/', views.celero_list_articles, name='celero_list_articles'),
    path('novo_artigo/', views.create_article, name='create_article'),
    path('editar/<str:id>', views.edit_article, name='edit_article'),
    path('deletar/<str:id>', views.delete_article, name='delete_article'),
    path('deletados/', views.list_deleted_articles, name='list_deleted_articles'),
    path('recuperar/<str:id>', views.recuperate_article, name='recuperate_article'),
]