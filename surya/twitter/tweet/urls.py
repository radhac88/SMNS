# from django.urls import path 
# from . import views

# urlpatterns = [
#     path('', views.user_list, name='user_list'),
#     path('log/', views.log_in, name='log_in'),
#     path('home/', views.home_list, name='home_list'),
#     path('sign/', views.signup, name='signup'),
# ]    
from django.urls import path
from . import views
urlpatterns = [
    path('', views.start, name='start'),
    path('signup/',views.signup,name='signup'),
    path('home/',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('logout/', views.logout, name='logout'),
]