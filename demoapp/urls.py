from django.urls import path
from . import views

urlpatterns =   [
    path('home/', views.home, name='home'),
    path('hotellist/', views.Hotels_List, name='hotellist'),
    path('hotellist/<str:pk>', views.hotel_detail, name='hoteldetail'),
    path('hotel_gen_list/', views.getGenericsList.as_view(), name='hotel_gen_list')

]