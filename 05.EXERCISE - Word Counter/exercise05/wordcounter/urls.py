from django import views
from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('wordcounter', views.wordcounter, name='wordcounter')
]