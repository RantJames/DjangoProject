from django.urls import path
from . import views

urlpatterns =   [
    path('home/', views.home, name='home'),
    path('hotellist/', views.Hotels_List, name='hotellist')
]