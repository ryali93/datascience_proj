from django.shortcuts import render

from django.views.generic import DetailView
from .models import City


class CitiesDetailView(DetailView):
    """
        City detail view.
    """
    template_name = 'cities/city-detail.html'
    model = City

def index(request):
    params = {}
    return render(request, 'index.html', params)
