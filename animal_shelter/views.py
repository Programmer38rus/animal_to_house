from django.shortcuts import render
from .models import Pet
from django.views.generic import (
    ListView,
    DetailView,
)


# Create your views here.

class PetsList(ListView):
    model = Pet
    template_name = 'base.html'
    context_object_name = 'Pets'


class PetsDetailView(DetailView):
    model = Pet
    template_name = 'base2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['pet'] = Pet.objects.all()
        return context
