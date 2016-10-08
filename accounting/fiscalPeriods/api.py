# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers, viewsets
from .models import FiscalPeriod
from .filters import FiscalPeriodFilter


# API

class FiscalPeriodSerializer(serializers.ModelSerializer):

    class Meta:
        model = FiscalPeriod
        fields = ('id', 'description',)


class FiscalPeriodViewSet(viewsets.ModelViewSet):

    serializer_class = FiscalPeriodSerializer
    queryset = FiscalPeriod.objects.all()
    lookup_field = 'id'
    filter_class = FiscalPeriodFilter

