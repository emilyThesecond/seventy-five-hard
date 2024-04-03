from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('diet/', views.diet, name="diet"),
    path('gallery/', views.gallery, name='gallery'),
    path('rules/', views.rules, name='rules')
]