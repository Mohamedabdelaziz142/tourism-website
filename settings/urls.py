from django.urls import path
from .views import home,home_search, category_filter, dashboard, news_letter_subscribe,place_filter
from .api_view import HomeAPIView, SettingAPIView,PropertyHomeSearchAPIView


app_name = 'settings'

urlpatterns = [
    path('', home , name='home'),
    path('search',home_search , name='home_search'),
    path('newsletter/', news_letter_subscribe, name='newsletter'),
    path('category/<slug:category>',category_filter , name='category_filter'),
    path('place/<str:place>',place_filter , name='place_filter'),
    path('dashboard/',dashboard , name='dashboard'),
     #api

    path('home/property/search',PropertyHomeSearchAPIView.as_view() , name='home_search_api'),   
    path('home/api',HomeAPIView.as_view() , name='home_api'),
    path('home/settings/api',SettingAPIView.as_view() , name='home_setting_api')
     
]
