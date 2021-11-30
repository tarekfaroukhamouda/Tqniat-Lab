from django.db.models import fields
from django.http import request
from django.http.response import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from .models import hotels,providers,amenities
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@login_required
@api_view(('GET',))
def getHotels(request):
    allHotels=[]
    singleHotel={}
    for hotel in hotels.objects.filter().values('id','provider','hotelName','rate','price'):
        provider=providers.objects.filter(id=hotel['provider'])[0]
        if provider.providerHotelKey==1:
            singleHotel['hotel']=hotel['hotelName']
        else:
            singleHotel['hotelname']=hotel['hotelName']
        if provider.ratetype==1:
            singleHotel['rate']=hotel["rate"] * "*"
        else:
            singleHotel['rate']=hotel["rate"]
        if provider.priceType=="1":
            singleHotel['Fare']=hotel['price']
        else:
            singleHotel['Price']=hotel['price']   
        all_amenties=[]
        for amenit in hotels.objects.filter(id=hotel['id']).values('amenities'):
            amenitName=amenities.objects.filter(id=amenit['amenities']).values('amenityName')[0]
            if provider.seprately==1:
                  all_amenties.append(amenitName['amenityName'])
                  singleHotel['amenities']=all_amenties
            else:
                  singleHotel.setdefault('roomAmenities','')
                  singleHotel['roomAmenities']+=str(amenitName['amenityName'])+","
        allHotels.append(singleHotel)
        singleHotel={}
    return Response(allHotels)
        
    
