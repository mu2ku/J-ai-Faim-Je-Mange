from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')

def recipes(request):
  return HttpResponse('<h1>Hello ᓚᘏᗢ</h1>')