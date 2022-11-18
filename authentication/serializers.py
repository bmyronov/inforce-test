from authentication.models import Employee, Restaurant, User

from rest_framework import serializers


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('restaurant_name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)

        user = self.Meta.model(**validated_data)

        if password is not None:
            user.set_password(password)

        user.is_restaurant = True
        user.save()

        Restaurant.objects.create(user=user)

        return user


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = self.Meta.model(**validated_data)

        if password is not None:
            user.set_password(password)

        user.is_employee = True
        user.save()

        Employee.objects.create(user=user)

        return user
