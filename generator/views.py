from django.shortcuts import render

import random

# Create your views here.
def index(request):
  return render(request, 'generator/index.html')

def about(request):
  return render(request, 'generator/about.html')

def password(request):
  characters = list('abcdefghijklmnñopqrstuvwxyz')
  generator_password = ''

  length = int(request.GET.get('length'))

  if request.GET.get('length'):
    characters.extend(list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'))
  if request.GET.get('special'):
    characters.extend(list('+-*/!|#$%&()=?¡¿}{.<>'))
  if request.GET.get('numbers'):
    characters.extend(list('0123456789'))

  for char in range(length):
    generator_password += random.choice(characters)

  return render(request, 'generator/password.html', {'password': generator_password})