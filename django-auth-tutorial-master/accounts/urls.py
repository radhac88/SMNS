from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('home/',views.home,name='home'),

]
# from django.urls import path

# from . import views


# urlpatterns = [
#     path('signup/', views.SignUp.as_view(), name='signup'),
#  	path('home/', views.home, name='home'),
       
# ]
