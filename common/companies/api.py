# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers, viewsets
from .models import Company
from .filters import CompanyFilter


# API

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('id', 'commercial_name', 'company_name', 'contact', 'financial_id', 'financial_accounting_id',
                  'phone_numbers', 'emails', 'logo', 'slogan',)


class CompanyViewSet(viewsets.ModelViewSet):

    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    lookup_field = 'id'
    filter_class = CompanyFilter
