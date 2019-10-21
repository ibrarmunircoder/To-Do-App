from django.urls import path
from . import views


app_name = 'todo-app'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('delete/(?<id>\d+)/', views.delete, name='delete'),
    path('cross_off/(?<id>\d+)/', views.cross_off, name='cross_off'),
    path('uncross/(?<id>\d+)/', views.uncross, name='uncross'),
    path('edit/(?<id>\d+)/', views.edit, name='edit'),
]
