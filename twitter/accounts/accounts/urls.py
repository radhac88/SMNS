from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('',views.home,name='home'),
    path('profile/<int:pk>/',views.profile, name='profile'),
  	path('updateprofile/',views.updateprofile,name='updateprofile'),
    path('comments/<int:pk>/',views.comments, name='comments'),
  	path('savecomment/<int:pk>/',views.savecomment, name='savecomment'),

]