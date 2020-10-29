from django.shortcuts import render
from .models import Pet, Kind
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
)


# Create your views here.
class PetsList(ListView):
    model = Pet
    template_name = 'base.html'
    context_object_name = 'Pets'


class KindList(ListView):
    model = Pet
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        pets = super().get_context_data(**kwargs)
        name_kind = self.kwargs['kind'].title()

        kind = Kind.objects.filter(name=name_kind).values()

        for id in kind:
            pets['Pets'] = Pet.objects.filter(kind=id['id'])
        return pets


class PetsDetailView(DetailView):
    model = Pet
    template_name = 'base2.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['pet'] = Pet.objects.all()
        return context

class AboutUs(TemplateView):
    template_name = 'about.html'
