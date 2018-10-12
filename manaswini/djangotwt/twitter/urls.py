from django.urls import path
from . import views
urlpatterns = [
    path('', views.start, name='start'),
    path('signup/',views.signup,name='signup'),
    path('home/',views.home,name='home'),
    path('login/<user>',views.login,name='login'),
    path('logout/', views.logout, name='logout'),
]