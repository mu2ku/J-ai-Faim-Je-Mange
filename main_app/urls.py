from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('profile/', views.profile, name='profile'),
  path('recipes/', views.recipes_index, name='recipes_index'),
  path('recipes/<letter>', views.recipes_index_letter, name='recipes_index_letter'),
  path('recipes/details/<recipe_name>/', views.recipes_detail,name='recipes_details'),
  path('recipes/create/', views.RecipeCreate.as_view(), name='recipes_create'),
  path('accounts/signup/', views.signup, name='signup'),
  path('recipes/details/<recipe_name>/assoc_user/<int:user_id>/', views.assoc_user, name='assoc_user'),
]