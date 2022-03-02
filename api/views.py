from multiprocessing import context
from re import I
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from api.models import Customer
from api.serializers import  CustomerSerializer
# from api.serializers import  CustomerSchema

    
class Customer_LC_API(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class  = CustomerSerializer

class Customer_RUD_API(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class  = CustomerSerializer