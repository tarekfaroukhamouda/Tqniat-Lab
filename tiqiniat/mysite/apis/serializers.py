from rest_framework import serializers
from .models import hotels,providers,amenities,cities

class providerSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = providers
        fields = ['providerName']

class amenitySerilaizer(serializers.ModelSerializer):
    class Meta:
        model=amenities
        fields=['amenityName']


class HotelSerializer(serializers.ModelSerializer):
   # amenities=amenitySerilaizer(many=True)
    class Meta:
        model = hotels
        fields = ['hotelName', 'rate', 'price']