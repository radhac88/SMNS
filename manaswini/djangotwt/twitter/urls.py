from django.urls import path
from . import views
# from django.conf.urls import include, url
urlpatterns = [
    path('', views.start, name='start'),
    path('signup/',views.signup,name='signup'),
    path('home/',views.home,name='home'),
    path('login/',views.user_log,name='user_log'),
    path('logout/', views.logout, name='logout'),
    path('follow/',views.follow, name="event_follow"),
]
# url(r'^event/(?P<event_id>\d+)/follow$', views.follow, name="event_follow"),