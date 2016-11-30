# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from.models import Product, ProductDepartment, ProductSubDepartment, ProductForSale


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ('id', 'code', 'description', 'department', 'subdepartment', 'useinventory', 'minimum', 'unit',
                    'cost', 'isactive', 'hasforsale')

    search_fields = ('id', 'code', 'description', 'department', 'subdepartment', 'useinventory', 'minimum', 'unit',
                     'cost', 'isactive', 'hasforsale')


@admin.register(ProductForSale)
class ProductAdmin(admin.ModelAdmin):

    list_display = ('id', 'code', 'company', 'product', 'barcode', 'description', 'department', 'subdepartment', 'utility', 'price',
                   'usetaxes', 'taxes', 'discount', 'sellprice', 'isactive',)

    search_fields = ('id', 'code', 'company', 'product__description', 'barcode', 'description', 'department', 'subdepartment', 'utility', 'price',
                     'usetaxes', 'taxes', 'discount', 'sellprice', 'isactive',)


@admin.register(ProductDepartment)
class ProductDepartmentAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'code',)
    search_fields = ('id', 'name', 'code',)


@admin.register(ProductSubDepartment)
class ProductSubDepartmentAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'department', 'code', )
    search_fields = ('id', 'name', 'department', 'code', )
