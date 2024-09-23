from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# Sempre me refiro como se estivesse na raiz
# Aí tenho que chamar assim importando.

def my_view(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Thiago Lima'
    })