from django.urls import path
from django.http import HttpResponse
from recipes.views import my_view

urlpatterns = [
    path('', my_view)
]