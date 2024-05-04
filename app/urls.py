from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('account/', views.account, name='account'),
    path('create_recipe/', views.create_recipe, name='create_recipe'),
]