from django.shortcuts import render
import requests

def home(request):
  return render(request, 'home.html')

def recipes_index(request):
  response = requests.get('http://www.themealdb.com/api/json/v1/1/search.php?f=a')
  recipes = response.json()
  return render(request, 'recipes/index.html', {
      'recipes': recipes['meals'],
  })