from django.db import models

class Recipe(models.Model):
  strMeal = models.CharField(max_length=255)
  strCategory = models.CharField(max_length=255)
  strArea= models.CharField(max_length=255)
  strInstructions = models.TextField()
  strThumb = models.CharField(max_length=255, default="https://picsum.photos/200/300.jpg")
  
  def __str__(self):
    return self.strMeal
  
  
  
  
