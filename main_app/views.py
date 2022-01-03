from django.shortcuts import render
from django.views.generic.edit import CreateView
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
  try:
    response = requests.get(f'http://www.themealdb.com/api/json/v1/1/search.php?f={letter}')
    recipes = response.json()
    dbrecipes = Recipe.objects.filter(strMeal__istartswith=letter)
    return render(request, 'recipes/index.html', {
        'recipes': recipes['meals'],
        'dbrecipes': dbrecipes,
    })
  except:
    pass
  
def recipes_detail(request, recipe_name):
  try:
    response = requests.get(f"http://www.themealdb.com/api/json/v1/1/search.php?s={recipe_name}")
    
    if(response is None):
      dbrecipe = Recipe.objects.filter(strMeal=recipe_name)
      return render(request, 'recipes/detail.html', {
          'dbrecipe': dbrecipe,
    })
    else:
      recipe = response.json()
      return render(request, 'recipes/detail.html', {
        'recipe': recipe['meals'][0],
    })
      
  except Exception as e:
    print(e)
    
class RecipeCreate(CreateView):
  model = Recipe
  fields = '__all__'
  success_url = '/recipes/'