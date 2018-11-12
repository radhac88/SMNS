from django.urls import path
from django.conf.urls import url
from . import views



urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('',views.home,name='home'),
    path('profile/<int:pk>/',views.profile, name='profile'),
  	path('updateprofile/',views.updateprofile,name='updateprofile'),

    # path('likes/<int:pk>/',views.likes, name='likes'),

    path('comments/<int:pk>/',views.comments, name='comments'),
  	path('savecomment/<int:pk>/',views.savecomment, name='savecomment'),

  	path('followers_page/',views.followers_page, name='followers_page'),
  	path('following_page/',views.following_page, name='following_page'),

  	path('search',views.search,name='search'),
  	path('autocomplete',views.autocomplete,name='ajax_autocomplete'),



]
