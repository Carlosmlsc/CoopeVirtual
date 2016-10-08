# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django_filters
from .models import FiscalPeriod


class FiscalPeriodFilter(django_filters.FilterSet):

    class Meta:
        model = FiscalPeriod
        fields = ('id', 'description',)
