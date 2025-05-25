from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    path('topics/', views.topics, name='topics'),

    # Página de detalhes para um único assunto
    path('topic/<int:topic_id>/', views.topic, name='topic'),

    # Página para adicionar um novo assunto
    path('new_topic/', views.new_topic, name='new_topic'),

    # Página para adicionar uma nova entrada
    path('new_entry/<topic_id>', views.new_entry, name='new_entry'),

    # Página para editar uma entrada
    path('edit_entry/<entry_id>/', views.edit_entry, name='edit_entry'),
]