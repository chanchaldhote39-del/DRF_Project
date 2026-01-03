from django.shortcuts import render
from rest_framework.response import Response
from .models import Product
from rest_framework.views import APIView
from rest_framework import mixins, generics
from .serializer import ProductSerializer
from rest_framework import status

from rest_framework import permissions
from rest_framework.views import APIView



# Create your views here.
# LIST + CREATE
class Product_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


# RETRIEVE + UPDATE + DELETE
class ProductDetialView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    def put(self, request, pk):
        return self.update(request, pk=pk)

    def delete(self, request, pk):
        return self.destroy(request, pk=pk)












# using generics

# # # LIST+CREATE
# class Product_list(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# # GET+UPDATE+DELETE
# class ProductDetialView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer   
#     lookup_field = 'pk'  