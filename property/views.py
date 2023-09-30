from django.shortcuts import redirect, render
from django.views.generic.edit import FormMixin
from django.views.generic import ListView, DetailView,CreateView
from .models import Property
from .forms import PropertyBookForm
from .filters import ProppertyFilter
from django_filters.views import FilterView


class PropertyList(FilterView):
    model = Property
    template_name = 'property/property_list.html' # Specify the template file for the list view
    paginate_by = 1
    filterset_class = ProppertyFilter

class PropertyView(FormMixin,DetailView):
    model = Property  # Specify the model for the detail view
    template_name = 'property/property_detail.html'  # Specify the template file for the detail viewView(DetailView):
    form_class = PropertyBookForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["related"] = Property.objects.filter(category = self.get_object().category)[:2]
        return context
    
    def post(self, request,*args,**kwargs):
        form = self.get_form()
        if form.is_valid():
            myform = form.save(commit= False)
            myform.property = self.get_object()
            myform.user = request.user
            myform.save()

            return redirect("/")
        
class AddListing(CreateView):
   pass