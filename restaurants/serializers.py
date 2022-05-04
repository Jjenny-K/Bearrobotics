from rest_framework import serializers
from restaurants.models import Restaurant, Guest

class RestaurantSerializer(serializers.ModelSerializer):
    """
        editor : 강정희
    """
    class Meta:
        model = Restaurant
        fields = (
            'name',
            'city',
            'address',
            'group',
        )

class GuestSerializer(serializers.ModelSerializer):
    """
        editor : 서재환
    """
    class Meta:
        model = Guest
        fields = (
            'restaurant',
            'price',
            'number_of_party',
            'timestamp',
            'payment'
        )

