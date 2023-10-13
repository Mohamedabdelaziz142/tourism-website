from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import FormMixin
from django.views.generic import ListView, DetailView,CreateView
from .models import Property,PropertyReview,PropertyImages,PropertyBook
from .forms import PropertyBookForm,PropertyReviewForm
from .filters import PropertyFilter
from django_filters.views import FilterView



class PropertyList(FilterView):
    model = Property
    template_name = 'property/property_list.html' # Specify the template file for the list view
    paginate_by = 3
    filterset_class = PropertyFilter

def property_detail(request, slug):
    property_instance = get_object_or_404(Property, slug=slug)
    related_properties = Property.objects.filter(category=property_instance.category).exclude(slug=property_instance.slug)[:2]
    reviews = PropertyReview.objects.filter(property=property_instance)
    images = PropertyImages.objects.filter(property=property_instance)

    if request.method == 'POST':
        form = PropertyBookForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.property = property_instance
            myform.user = request.user
            myform.save()
            booking_instance = PropertyBook.objects.filter(property=property_instance, user=request.user).last()
            return redirect(f"{booking_instance.id}/booked")
    else:
        form = PropertyBookForm()

    context = {
        'property': property_instance,  
        'related': related_properties,
        'reviews': reviews,
        'form': form,
        'images':images
    }
    return render(request, 'property/property_detail.html', context)
     
def property_review(request, pk):
    if request.method == 'POST':
        form = PropertyReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.property_id = pk
            review.save()
            return redirect(f'/property/{review.property.slug}')
    else:
        form = PropertyReviewForm()
    
    return render(request, 'property/property_review.html', {'form': form})

def successful_booking(request, pk):
    booking_instance = get_object_or_404(PropertyBook, id=pk)
    date_to = booking_instance.date_to
    date_from = booking_instance.date_from
    name = booking_instance.property.name
    price = booking_instance.property.price
    place = booking_instance.property.place.name
    owner = booking_instance.property.owner

    number_of_days = date_to - date_from
    number_of_days_seconds = number_of_days.total_seconds()
    number_of_days_in_integers = int(number_of_days_seconds // (24 * 60 * 60))
    total_price = number_of_days_in_integers * price


    context ={
        'date_to':date_to,
        'date_from':date_from,
        'place':place,
        'owner':owner,
        'name':name,
        'price':price,
        'nights':number_of_days_in_integers,
        'total_price':total_price
    } 
    return render(request, 'property/property_booked.html', context)
