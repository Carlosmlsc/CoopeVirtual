# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from.models import Product, ProductDepartment, ProductSubDepartment


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ('id', 'code', 'barcode', 'description', 'department', 'subdepartment', 'useinventory', 'inventory',
                    'minimum', 'sellmethod', 'cost', 'autoprice', 'utility','price', 'usetaxes', 'taxes', 'discount',
                    'sellprice',)

    search_fields = ('id', 'code', 'barcode', 'description', 'department__name', 'subdepartment__name', 'useinventory',
                     'inventory', 'minimum', 'sellmethod', 'cost', 'autoprice', 'utility','price', 'usetaxes', 'taxes',
                     'discount', 'sellprice',)


@admin.register(ProductDepartment)
class ProductDepartmentAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'code',)
    search_fields = ('id', 'name', 'code',)


@admin.register(ProductSubDepartment)
class ProductSubDepartmentAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'department', 'code', )
    search_fields = ('id', 'name', 'department', 'code', )
