from django.http.response import Http404
from rest_framework.views import APIView
from onlineshop.models import Brand, Category, Product
from onlineshop.api.serializers import BrandModelSerializer, CategoryModelSerializer,ProductModelSerilizer
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework import generics, mixins, viewsets
from rest_framework.permissions import IsAuthenticated



class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandModelSerializer
    # permission_classes = [IsAuthenticated]



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    # permission_classes = [IsAuthenticated]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerilizer
    # permission_classes = [IsAuthenticated]



