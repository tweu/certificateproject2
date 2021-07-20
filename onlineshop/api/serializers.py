
from django.db.models import query
from django.db.models.query import QuerySet
from onlineshop.models import Brand, Category, Product
from django.http import request
from rest_framework import serializers


class BrandModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = '__all__'
        # read_only_fields = ('creator', )


class CategoryModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
        # read_only_fields = ('creator', )


class ProductModelSerilizer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
        # read_only_fields = ('creator', )


    def to_representation(self, instance):
        data = super().to_representation(instance)
        # data['group'] = GroupModelSerializer(instance.group).data
        data['brand'] = BrandModelSerializer(instance.brand).data
        return data

