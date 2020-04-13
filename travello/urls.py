
from django.urls import path
from . import views


urlpatterns=[
    path('',views.index,name='index'),
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signup'),
    path('user/<str:pk>/',views.userPage,name='user_page'),
    path('about/',views.about,name='about'),
    path('',views.signout,name='signout'),
    path('reservations/<str:pk>/',views.reservations,name='reservations'),

]


