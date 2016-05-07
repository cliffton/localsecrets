from rest_framework import serializers
from django.contrib.auth.models import User
from accounts.models import Customer, Vendor


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
