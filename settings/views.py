from django.contrib.auth.models import User
from django.shortcuts import render
from property.models import Property, Place, Category
from blog.models import Post
from django.db.models import Count

# Create your views here.

def home(request):
    place = Place.objects.all().annotate(property_count=Count('property_place'))
    category = Category.objects.all()

    resturant_list = Property.objects.filter(category__name ='Restaurants')[:5]
    hotels_list =  Property.objects.filter(category__name= 'Hotels')[:4]
    places_list =  Property.objects.filter(category__name= 'Places')[:4]
    recent_posts = Post.objects.all()[:4]

    users_count = User.objects.count()
    places_count = Property.objects.filter(category__name= 'Places').count()
    resturants_count = Property.objects.filter(category__name ='Restaurants').count()
    hotels_count = Property.objects.filter(category__name= 'Hotels').count()


    return render(request,'settings/home.html',{
        'places':place,
        'category':category,
        'resturant_list':resturant_list,
        'hotels_list':hotels_list,
        'places_list':places_list,
        'recent_posts':recent_posts,
        'users_count':users_count,
        'places_count':places_count,
        'resturants_count':resturants_count,
        'hotels_count':hotels_count

        
    })



def home_search(request):
    name = request.GET.get('name')
    place = request.GET.get('place')

    property_list = Property.objects.all()

    if name:
        property_list = property_list.filter(name__icontains=name)
    if place:
        property_list = property_list.filter(place__name__icontains=place)

    return render(request, 'settings/home_search.html', {'property_list': property_list})
    
def category_filter(request, category):
   category = Category.objects.get(name=category)
   property_list = Property.objects.filter(category=category)
   return render(request, 'settings/home_search.html', {'property_list': property_list})


def contact_us(request):
    pass