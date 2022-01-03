from django.shortcuts import render
from .models import Recipe
import requests

def home(request):
  return render(request, 'home.html')

def recipes_index(request):
  response = requests.get('http://www.themealdb.com/api/json/v1/1/search.php?f=a')
  recipes = response.json()
  dbrecipes = Recipe.objects.all()
  return render(request, 'recipes/index.html', {
      'recipes': recipes['meals'],
      'dbrecipes': dbrecipes,
  })

def recipes_index_letter(request, letter):
  response = requests.get(f'http://www.themealdb.com/api/json/v1/1/search.php?f={letter}')
  recipes = response.json()
  dbrecipes = Recipe.objects.filter(strMeal__istartswith=letter)
  return render(request, 'recipes/index.html', {
      'recipes': recipes['meals'],
      'dbrecipes': dbrecipes,
  })
  
def recipes_detail(request, recipe_name):
  response = requests.get(f"http://www.themealdb.com/api/json/v1/1/search.php?s={recipe_name}")
  recipe = response.json()
  return render(request, 'recipes/detail.html', {
      'recipe': recipe['meals'][0],
  })