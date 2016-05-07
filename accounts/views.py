from django.shortcuts import render
from rest_framework import status

# Create your views here.
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import serializers
from accounts.models import Customer, Vendor
from accounts.serializers import UserSerializer, CustomerSerializer, VendorSerializer
from rest_framework.generics import CreateAPIView


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class VendorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class UserRegisterView(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        # import pdb; pdb.set_trace()
        data = dict()
        try:
            data = {
                'username': request.data['name'],
                'email': request.data['email']
            }
            user = User(**data)
            user.save()
            customer = Customer(user=user, age=request.data['age'], gender=request.data['gender'])
            customer.save()
            response = UserSerializer(user).data

            return Response(
                response,
                status=status.HTTP_201_CREATED)
        except KeyError:
            raise serializers.ValidationError({"Invalid JSON": "Blah"})

    def get_serializer(self, *args, **kwargs):
        return super(UserRegisterView, self).get_serializer(*args, **kwargs)
