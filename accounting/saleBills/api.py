# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers, viewsets
from .models import SaleBill, SaleBillDetail
from .filters import SaleBillFilter, SaleBillDetailFilter


# API

class SaleBillSerializer(serializers.ModelSerializer):

    class Meta:
        model = SaleBill
        fields = ('id', 'company', 'sale_num', 'date', 'currency', 'client', 'sub_total', 'discount', 'exempt',
                  'tax_amount', 'total', )


class SaleBillViewSet(viewsets.ModelViewSet):

    serializer_class = SaleBillSerializer
    queryset = SaleBill.objects.all()
    lookup_field = 'id'
    filter_class = SaleBillFilter



class SaleBillDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = SaleBillDetail
        fields = ('id', 'sale_bill', 'product_code', 'qty', 'description', 'use_taxes', 'tax_percentage', 'unit_price',
                  'subtotal', )


class SaleBillDetailViewSet(viewsets.ModelViewSet):

    serializer_class = SaleBillDetailSerializer
    queryset = SaleBillDetail.objects.all()
    lookup_field = 'id'
    filter_class = SaleBillDetailFilter
