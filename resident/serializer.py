from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from resident.models import House


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['username', "first_name", "last_name", "email", "phone", "password"]

class HouseSerializer(serializers.ModelSerializer):
    user = serializers.IntegerField()
    class Meta:
        model = House
        fields = ['house_number', 'apartment_number', 'street_name']

class CreateInviteSerializer(serializers.Serializer):
    code = models.CharField(max_length=6, default=generate_code, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(null=False, blank=False)
    status = models.BooleanField(default=True)
    house = models.ForeignKey(House, on_delete=models.PROTECT)
