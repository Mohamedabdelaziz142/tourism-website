from django.urls import path
from .views import PropertyList, PropertyView

app_name = 'property'

urlpatterns = [
    path('',PropertyList.as_view(), name='property_list'),
    path('<slug:slug>', PropertyView.as_view(), name='property_detail')
]