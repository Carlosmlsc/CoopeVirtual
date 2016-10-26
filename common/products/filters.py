# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django_filters
from .models import Product, ProductDepartment, ProductSubDepartment


class ProductFilter(django_filters.FilterSet):

    class Meta:
        model = Product
        fields = ('id', 'company', 'code', 'barcode', 'description', 'department', 'subdepartment', 'useinventory',
                  'inventory', 'minimum', 'sellmethod', 'cost', 'autoprice', 'utility','price', 'usetaxes', 'taxes',
                  'discount', 'sellprice',)


class ProductDepartmentFilter(django_filters.FilterSet):

    class Meta:
        model = ProductDepartment
        fields = ('id', 'name', 'code',)


class ProductSubDepartmentFilter(django_filters.FilterSet):

    class Meta:
        model = ProductSubDepartment
        fields = ('id', 'name', 'department', 'code', )
