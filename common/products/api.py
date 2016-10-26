# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers, viewsets
from .models import Product, ProductDepartment, ProductSubDepartment
from .filters import ProductFilter, ProductDepartmentFilter, ProductSubDepartmentFilter


# API

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'company', 'code', 'barcode', 'description', 'department', 'subdepartment', 'useinventory', 'inventory',
                  'minimum', 'sellmethod', 'cost', 'autoprice', 'utility','price', 'usetaxes', 'taxes', 'discount',
                  'sellprice',)


class ProductViewSet(viewsets.ModelViewSet):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'id'
    filter_class = ProductFilter


class ProductDepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductDepartment
        fields = ('id', 'name', 'code',)


class ProductDepartmentViewSet(viewsets.ModelViewSet):

    serializer_class = ProductDepartmentSerializer
    queryset = ProductDepartment.objects.all()
    lookup_field = 'id'
    filter_class = ProductDepartmentFilter


class ProductSubDepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductSubDepartment
        fields = ('id', 'name', 'department', 'code', )


class ProductSubDepartmentViewSet(viewsets.ModelViewSet):

    serializer_class = ProductSubDepartmentSerializer
    queryset = ProductSubDepartment.objects.all()
    lookup_field = 'id'
    filter_class = ProductSubDepartmentFilter
