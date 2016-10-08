# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django_filters
from .models import Currency


class CurrencyFilter(django_filters.FilterSet):

    class Meta:
        model = Currency
        fields = ('id', 'name', 'symbol', )
