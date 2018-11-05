from django.urls import path
from django.conf.urls import url
from . import views



urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('',views.home,name='home'),
    path('profile/<int:pk>/',views.profile, name='profile'),
  	path('updateprofile/',views.updateprofile,name='updateprofile'),

]

