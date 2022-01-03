from django.shortcuts import render

def home(request):
  return render(request, 'home.html')

def recipes(request):
  return render(request, 'recipes/recipes_index.html')