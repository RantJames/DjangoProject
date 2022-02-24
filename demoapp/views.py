from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import HotelSerializer

from .models import Hotels


def home(request):
    return HttpResponse("<h1>HELLO WORLD<h1>")


@api_view(['GET', 'POST'])
def Hotels_List(request):
    if request.method == 'GET':
        hotels_list = Hotels.objects.all()
        hotelserializer = HotelSerializer(hotels_list, many=True)
        return Response(hotelserializer.data)
    if request.method == 'POST':
        request_data = request.data
        serialize_request_data = HotelSerializer(data=request_data)
        if serialize_request_data.is_valid():
            serialize_request_data.save()
        return Response({"Message": "Added Successfully"})