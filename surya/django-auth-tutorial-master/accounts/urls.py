from django.urls import path

from . import views
from django.conf.urls import url
 



urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('',views.home,name='home'),
    path('profile/<int:pk>/',views.profile, name='profile'),
  	path('updateprofile/',views.updateprofile,name='updateprofile'),
  	 # path('user_log/',views.home,name='login'),
    
]
# from django.urls import path

# from . import views


# urlpatterns = [
#     path('signup/', views.SignUp.as_view(), name='signup'),
#  	path('home/', views.home, name='home'),
       
# ]
