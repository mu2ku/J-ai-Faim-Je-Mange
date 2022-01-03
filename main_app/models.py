from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  strMeal = models.CharField(max_length=255)
  strCategory = models.CharField(max_length=255, blank=True, null=True)
  strArea= models.CharField(max_length=255, blank=True, null=True)
  strInstructions = models.TextField()
  strThumb = models.CharField(max_length=255, default="https://picsum.photos/200/300.jpg", blank=True, null=True)
  strIngredient1= models.CharField(max_length=255, default="", blank=True, null=True)
  strIngredient2= models.CharField(max_length=255, default="", blank=True, null=True)
  strIngredient3= models.CharField(max_length=255, default="", blank=True, null=True)
  strIngredient4= models.CharField(max_length=255, default="", blank=True, null=True)
  strIngredient5= models.CharField(max_length=255, default="", blank=True, null=True)
  strIngredient6= models.CharField(max_length=255, default="", blank=True, null=True)
  strIngredient7= models.CharField(max_length=255, default="", blank=True, null=True)
  strIngredient8= models.CharField(max_length=255, default="", blank=True, null=True)
  strIngredient9= models.CharField(max_length=255, default="", blank=True, null=True)
  strIngredient10= models.CharField(max_length=255, default="", blank=True, null=True)
  strIngredient11= models.CharField(max_length=255, default="", blank=True, null=True)
  strIngredient12= models.CharField(max_length=255, default="", blank=True, null=True)
  strIngredient13= models.CharField(max_length=255, default="", blank=True, null=True)
  strIngredient14= models.CharField(max_length=255, default="", blank=True, null=True)
  strIngredient15= models.CharField(max_length=255, default="", blank=True, null=True)
  strIngredient16= models.CharField(max_length=255, default="", blank=True, null=True)
  strIngredient17= models.CharField(max_length=255, default="", blank=True, null=True)
  strIngredient18= models.CharField(max_length=255, default="", blank=True, null=True)
  strIngredient19= models.CharField(max_length=255, default="", blank=True, null=True)
  strIngredient20= models.CharField(max_length=255, default="", blank=True, null=True)
  strIngredient21= models.CharField(max_length=255, default="", blank=True, null=True)
  strIngredient22= models.CharField(max_length=255, default="", blank=True, null=True)
  strIngredient23= models.CharField(max_length=255, default="", blank=True, null=True)
  strIngredient24= models.CharField(max_length=255, default="", blank=True, null=True)
  strIngredient25= models.CharField(max_length=255, default="", blank=True, null=True)
  strIngredient26= models.CharField(max_length=255, default="", blank=True, null=True)
  strIngredient27= models.CharField(max_length=255, default="", blank=True, null=True)
  strIngredient28= models.CharField(max_length=255, default="", blank=True, null=True)
  strIngredient29= models.CharField(max_length=255, default="", blank=True, null=True)
  strIngredient30= models.CharField(max_length=255, default="", blank=True, null=True)
  strIngredient31= models.CharField(max_length=255, default="", blank=True, null=True)
  strIngredient32= models.CharField(max_length=255, default="", blank=True, null=True)
  strIngredient33= models.CharField(max_length=255, default="", blank=True, null=True)
  strIngredient34= models.CharField(max_length=255, default="", blank=True, null=True)
  strIngredient35= models.CharField(max_length=255, default="", blank=True, null=True)
  strIngredient36= models.CharField(max_length=255, default="", blank=True, null=True)
  strIngredient37= models.CharField(max_length=255, default="", blank=True, null=True)
  strIngredient38= models.CharField(max_length=255, default="", blank=True, null=True)
  strIngredient39= models.CharField(max_length=255, default="", blank=True, null=True)
  strIngredient40= models.CharField(max_length=255, default="", blank=True, null=True)
 
  def __str__(self):
    return self.strMeal
  
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  recipes = models.ForeignKey(Recipe, on_delete=models.CASCADE)
  
  
  
  
