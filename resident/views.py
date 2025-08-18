from rest_framework import status
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.utils import timezone
from datetime import timedelta

from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from resident.models import User, House
from resident.serializer import HouseSerializer


# Create your views here.

@api_view(['POST'])
def add_house(request):
    serializer = HouseSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = get_object_or_404(User, pk=serializer.validated_data['user'])
    if user.is_resident:
        House.objects.create(
            house_number=serializer.validated_data['house_number'],
            apartment_number=serializer.validated_data['apartment_number'],
            street_name=serializer.validated_data['street_name'],
            user=serializer.validated_data['user'],
        )
        serializer.save()
        return Response(data={"message": "House added successfully"}, status=status.HTTP_201_CREATED)

    print(user)
    return Response(data={"message": "Not Authorized"}, status=status.HTTP_403_FORBIDDEN)

@api_view()
def create_resident(request):
    return HttpResponse("Created Successfully")


def get_expiry_time() :
    return timezone.now() + timedelta(hours=10)
