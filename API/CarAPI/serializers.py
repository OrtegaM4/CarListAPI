from rest_framework import serializers
from .models import Cars
from django.contrib.auth.models import User


class CarSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Cars
        fields = ("make", "name","horsepower",)#'owner')

# class UserSerializer(serializers.ModelSerializer):
#     cars = serializers.PrimaryKeyRelatedField(many=True, queryset=Cars.objects.all())
#
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'cars')
