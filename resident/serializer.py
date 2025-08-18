from rest_framework import serializers

class HouseSerializer(serializers.Serializer):
    house_number = serializers.IntegerField()
    apartment_number = serializers.IntegerField()
    street_name = serializers.CharField()
    user = serializers.IntegerField()
