from rest_framework import serializers

from resident.models import House


class HouseSerializer(serializers.Serializer):
    class Meta:
        model = House
        li
    house_number = serializers.IntegerField()
    apartment_number = serializers.IntegerField()
    street_name = serializers.CharField()
    user = serializers.IntegerField()
