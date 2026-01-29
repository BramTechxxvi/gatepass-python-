from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from resident.models import House, Invite, Visitor


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['username', "first_name", "last_name", "email", "phone", "password"]


class HouseSerializer(serializers.ModelSerializer):
    user = serializers.IntegerField()
    class Meta:
        model = House
        fields = ['house_number', 'apartment_number', 'street_name']


class InviteSerializer(serializers.ModelSerializer):
    house = serializers.IntegerField()
    class Meta:
        model = Invite
        fields = ['code', 'created_at', 'expires_at', 'status']


class VisitorSerializer(serializers.ModelSerializer):
    invite = serializers.IntegerField()
    class Meta:
        model = Visitor
        fields = ['first_name', 'last_name', 'phone']