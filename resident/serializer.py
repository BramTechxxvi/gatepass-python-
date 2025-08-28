from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from resident.models import House


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['username', "first_name", "last_name", "email", "phone", "password"]

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = []
    house_number = serializers.IntegerField()
    apartment_number = serializers.IntegerField()
    street_name = serializers.CharField()
    user = serializers.IntegerField()
