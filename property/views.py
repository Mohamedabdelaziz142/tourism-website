from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Property

class PropertyList(ListView):
    model = Property
    template_name = 'property/property_list.html'  # Specify the template file for the list view


class PropertyView(DetailView):
    model = Property  # Specify the model for the detail view
    template_name = 'property/property_detail.html'  # Specify the template file for the detail viewView(DetailView):
  
  #book