# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django_filters
from .models import Company


class CompanyFilter(django_filters.FilterSet):

    class Meta:
        model = Company
        fields = ('id', 'commercial_name', 'company_name', 'contact', 'financial_id', 'financial_accounting_id',
                  'phone_numbers', 'emails', 'slogan',)
