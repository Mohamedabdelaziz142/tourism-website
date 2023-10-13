from django.urls import path
from .views import PropertyList, property_review,property_detail,successful_booking
from .api_view import PropertyApiList, PropertyApiDetail

app_name = 'property'

urlpatterns = [
    path('',PropertyList.as_view(), name='property_list'),
    path('<slug:slug>', property_detail, name='property_detail'),
    path('<int:pk>/review', property_review, name='property_review'),
    path('<int:pk>/booked', successful_booking, name='property_booked'),


     
     #api
    path('api/list', PropertyApiList.as_view(), name='property_api_list'),
    path('api/list/<int:pk>', PropertyApiDetail.as_view(), name='property_api_detail'),
]