from django.urls import path
from .views import register,profile,myreservation,mylisting
from django.contrib.auth import views as auth_views

app_name= 'accounts'
urlpatterns = [
     path('', register,name="register"),
     path('profile/',profile,name="profile"),
     path('reservation/',myreservation,name="reservation"),
     path('listing/',mylisting,name="listing"),
     path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
     path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'),name='logout'),
]