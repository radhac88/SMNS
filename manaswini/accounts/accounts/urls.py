from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
 	path('home/', views.home, name='home'),
 	# path('new/',views.new,name='new'),
 	path('profile/<int:pk>/',views.profile, name='profile'),
      
]