# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django_filters
from .models import SaleBill, SaleBillDetail


class SaleBillFilter(django_filters.FilterSet):

    class Meta:
        model = SaleBill
        fields = ('id', 'company', 'sale_num', 'date', 'currency', 'client', 'sub_total', 'discount', 'exempt',
                  'tax_amount', 'total', )


class SaleBillDetailFilter(django_filters.FilterSet):

    class Meta:
        model = SaleBillDetail
        fields = ('id', 'sale_bill', 'product_code', 'qty', 'description', 'use_taxes', 'tax_percentage', 'unit_price',
                  'subtotal', )
