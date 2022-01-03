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
  
def recipes_index_a(request):
  response = requests.get('http://www.themealdb.com/api/json/v1/1/search.php?f=a')
  recipes = response.json()
  return render(request, 'recipes/index.html', {
      'recipes': recipes['meals'],
  })

def recipes_index_b(request):
  response = requests.get('http://www.themealdb.com/api/json/v1/1/search.php?f=b')
  recipes = response.json()
  return render(request, 'recipes/index.html', {
      'recipes': recipes['meals'],
  })
  
def recipes_index_c(request):
  response = requests.get('http://www.themealdb.com/api/json/v1/1/search.php?f=c')
  recipes = response.json()
  return render(request, 'recipes/index.html', {
      'recipes': recipes['meals'],
  })

def recipes_index_d(request):
  response = requests.get('http://www.themealdb.com/api/json/v1/1/search.php?f=d')
  recipes = response.json()
  return render(request, 'recipes/index.html', {
      'recipes': recipes['meals'],
  })
  
def recipes_index_e(request):
  response = requests.get('http://www.themealdb.com/api/json/v1/1/search.php?f=e')
  recipes = response.json()
  return render(request, 'recipes/index.html', {
      'recipes': recipes['meals'],
  })
  
def recipes_index_f(request):
  response = requests.get('http://www.themealdb.com/api/json/v1/1/search.php?f=f')
  recipes = response.json()
  return render(request, 'recipes/index.html', {
      'recipes': recipes['meals'],
  })
  
def recipes_index_g(request):
  response = requests.get('http://www.themealdb.com/api/json/v1/1/search.php?f=g')
  recipes = response.json()
  return render(request, 'recipes/index.html', {
      'recipes': recipes['meals'],
  })
  
def recipes_index_h(request):
  response = requests.get('http://www.themealdb.com/api/json/v1/1/search.php?f=h')
  recipes = response.json()
  return render(request, 'recipes/index.html', {
      'recipes': recipes['meals'],
  })
  
def recipes_index_i(request):
  response = requests.get('http://www.themealdb.com/api/json/v1/1/search.php?f=i')
  recipes = response.json()
  return render(request, 'recipes/index.html', {
      'recipes': recipes['meals'],
  })
  
def recipes_index_j(request):
  response = requests.get('http://www.themealdb.com/api/json/v1/1/search.php?f=j')
  recipes = response.json()
  return render(request, 'recipes/index.html', {
      'recipes': recipes['meals'],
  })
  
def recipes_index_k(request):
  response = requests.get('http://www.themealdb.com/api/json/v1/1/search.php?f=k')
  recipes = response.json()
  return render(request, 'recipes/index.html', {
      'recipes': recipes['meals'],
  })
  
def recipes_index_l(request):
  response = requests.get('http://www.themealdb.com/api/json/v1/1/search.php?f=l')
  recipes = response.json()
  return render(request, 'recipes/index.html', {
      'recipes': recipes['meals'],
  })
  
def recipes_index_m(request):
  response = requests.get('http://www.themealdb.com/api/json/v1/1/search.php?f=m')
  recipes = response.json()
  return render(request, 'recipes/index.html', {
      'recipes': recipes['meals'],
  })
  
def recipes_index_n(request):
  response = requests.get('http://www.themealdb.com/api/json/v1/1/search.php?f=n')
  recipes = response.json()
  return render(request, 'recipes/index.html', {
      'recipes': recipes['meals'],
  })
  
def recipes_index_o(request):
  response = requests.get('http://www.themealdb.com/api/json/v1/1/search.php?f=o')
  recipes = response.json()
  return render(request, 'recipes/index.html', {
      'recipes': recipes['meals'],
  })
  
def recipes_index_p(request):
  response = requests.get('http://www.themealdb.com/api/json/v1/1/search.php?f=p')
  recipes = response.json()
  return render(request, 'recipes/index.html', {
      'recipes': recipes['meals'],
  })
  
def recipes_index_q(request):
  response = requests.get('http://www.themealdb.com/api/json/v1/1/search.php?f=q')
  recipes = response.json()
  return render(request, 'recipes/index.html', {
      'recipes': recipes['meals'],
  })
  
def recipes_index_r(request):
  response = requests.get('http://www.themealdb.com/api/json/v1/1/search.php?f=r')
  recipes = response.json()
  return render(request, 'recipes/index.html', {
      'recipes': recipes['meals'],
  })
  
def recipes_index_s(request):
  response = requests.get('http://www.themealdb.com/api/json/v1/1/search.php?f=s')
  recipes = response.json()
  return render(request, 'recipes/index.html', {
      'recipes': recipes['meals'],
  })
  
def recipes_index_t(request):
  response = requests.get('http://www.themealdb.com/api/json/v1/1/search.php?f=t')
  recipes = response.json()
  return render(request, 'recipes/index.html', {
      'recipes': recipes['meals'],
  })
  
def recipes_index_u(request):
  response = requests.get('http://www.themealdb.com/api/json/v1/1/search.php?f=u')
  recipes = response.json()
  return render(request, 'recipes/index.html', {
      'recipes': recipes['meals'],
  })
  
def recipes_index_v(request):
  response = requests.get('http://www.themealdb.com/api/json/v1/1/search.php?f=v')
  recipes = response.json()
  return render(request, 'recipes/index.html', {
      'recipes': recipes['meals'],
  })
  
def recipes_index_w(request):
  response = requests.get('http://www.themealdb.com/api/json/v1/1/search.php?f=w')
  recipes = response.json()
  return render(request, 'recipes/index.html', {
      'recipes': recipes['meals'],
  })
  
def recipes_index_x(request):
  response = requests.get('http://www.themealdb.com/api/json/v1/1/search.php?f=x')
  recipes = response.json()
  return render(request, 'recipes/index.html', {
      'recipes': recipes['meals'],
  })
  
def recipes_index_y(request):
  response = requests.get('http://www.themealdb.com/api/json/v1/1/search.php?f=y')
  recipes = response.json()
  return render(request, 'recipes/index.html', {
      'recipes': recipes['meals'],
  })
  
def recipes_index_z(request):
  response = requests.get('http://www.themealdb.com/api/json/v1/1/search.php?f=z')
  recipes = response.json()
  return render(request, 'recipes/index.html', {
      'recipes': recipes['meals'],
  })
  
def recipes_detail(request, recipe_name):
  response = requests.get(f"http://www.themealdb.com/api/json/v1/1/search.php?s={recipe_name}")
  recipe = response.json()
  return render(request, 'recipes/detail.html', {
      'recipe': recipe['meals'][0],
  })