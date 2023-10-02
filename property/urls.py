from django.urls import path
from .views import PropertyList, PropertyView
from .api_view import PropertyApiList, PropertyApiDetail

app_name = 'property'

urlpatterns = [
    path('',PropertyList.as_view(), name='property_list'),
    path('<slug:slug>', PropertyView.as_view(), name='property_detail'),
     
     #api
    path('api/list', PropertyApiList.as_view(), name='property_api_list'),
    path('api/list/<int:pk>', PropertyApiDetail.as_view(), name='property_api_detail'),
]