from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Recipe
import requests

class Home(LoginView):
  template_name = 'home.html'
  
def profile(request):
  recipes = Recipe.objects.filter(users=request.user)
  return render(request, 'profile.html', { 'recipes': recipes})

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
    res = requests.get(f'http://www.themealdb.com/api/json/v1/1/search.php?f={letter}')
    recipes = res.json()
    dbrecipes = Recipe.objects.filter(strMeal__istartswith=letter)
    return render(request, 'recipes/index.html', {
        'recipes': recipes['meals'],
        'dbrecipes': dbrecipes,
    })
  except:
    pass
  
def recipes_detail(request, recipe_name):
  try:
    user = request.user
    res = requests.get(f"http://www.themealdb.com/api/json/v1/1/search.php?s={recipe_name}")
    recipe = res.json()
    return render(request, 'recipes/detail.html', {
      'recipe': recipe['meals'][0],
      'user': user
    })
      
  except:
    user = request.user
    dbrecipe = Recipe.objects.get(strMeal=recipe_name)
    return render(request, 'recipes/detail.html', {
          'dbrecipe': dbrecipe,
          'user': user
    })
    
class RecipeCreate(CreateView):
  model = Recipe
  fields = ['strMeal', 'strCategory', 'strArea', 'strInstructions', 'strThumb', 'strIngredient1', 'strIngredient2', 'strIngredient3', 'strIngredient4', 'strIngredient5', 'strIngredient6', 'strIngredient7', 'strIngredient8', 'strIngredient9', 'strIngredient10', 'strIngredient11', 'strIngredient12', 'strIngredient13', 'strIngredient14', 'strIngredient15','strIngredient16', 'strIngredient17', 'strIngredient18', 'strIngredient19', 'strIngredient20', 'strIngredient21', 'strIngredient22', 'strIngredient23', 'strIngredient24', 'strIngredient25', 'strIngredient26', 'strIngredient27', 'strIngredient28', 'strIngredient29', 'strIngredient30','strIngredient31', 'strIngredient32', 'strIngredient33', 'strIngredient34', 'strIngredient35', 'strIngredient36', 'strIngredient37', 'strIngredient38', 'strIngredient39', 'strIngredient40']
  success_url = '/recipes/'
  
def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('recipes_index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)

def assoc_user(request, recipe_name, user_id):
  Recipe.objects.get(strMeal=recipe_name).users.add(user_id)
  return redirect(f'/recipes/details/{recipe_name}/')