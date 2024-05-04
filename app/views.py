from django.shortcuts import render, HttpResponse
from .models import TodoItem

# Create your view here

def home(request):
    return render(request, 'home.html')

def account(request):
    return render(request, 'account.html')

def create_recipe(request):
    return render(request, 'create_recipe.html')

# def todos(request):
#     items = TodoItem.objects.all()
#     return render(request, 'todos.html', {'todos': items})
