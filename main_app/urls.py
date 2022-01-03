from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('recipes/', views.recipes_index, name='recipes_index'),
  path('recipes/<letter>', views.recipes_index_letter, name='recipes_index_letter'),
  path('recipes/details/<recipe_name>/', views.recipes_detail,name='recipes_details'),
  path('recipes/create/', views.RecipeCreate.as_view(), name='recipes_create'),
]