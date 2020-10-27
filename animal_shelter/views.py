from django.shortcuts import render
from .models import Pet
from django.views.generic import ListView
# Create your views here.

class PetsList(ListView):
    model = Pet
    template_name = 'base.html'
    context_object_name = 'Pets'