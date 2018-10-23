from django.urls import path
from . import views
urlpatterns = [
    path('', views.start, name='start'),
    path('signup/',views.signup,name='signup'),
    path('home/',views.home,name='home'),
    path('login/',views.user_login,name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('search/', views.search, name='search'),
]