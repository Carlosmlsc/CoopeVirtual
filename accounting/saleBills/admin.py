# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin
from .models import SaleBill, SaleBillDetail


@admin.register(SaleBill)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'sale_num', 'date', 'currency', 'client', 'sub_total', 'discount', 'exempt',
                    'tax_amount', 'total', )

    search_fields = ('id', 'company', 'sale_num', 'date', 'currency', 'client', 'sub_total', 'discount', 'exempt',
                     'tax_amount', 'total', )


@admin.register(SaleBillDetail)
class EntryDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'sale_bill', 'product_code', 'qty', 'description', 'use_taxes', 'tax_percentage',
                    'unit_price', 'subtotal', )
    search_fields = ('id', 'sale_bill', 'product_code', 'qty', 'description', 'use_taxes', 'tax_percentage',
                     'unit_price', 'subtotal', )
