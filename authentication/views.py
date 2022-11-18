from authentication.serializers import EmployeeSerializer, RestaurantSerializer
from authentication.models import User

from rest_framework import generics


class RestaurantRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RestaurantSerializer


class EmployeeRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = EmployeeSerializer
