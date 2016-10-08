# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers, viewsets
from .models import Currency
from .filters import CurrencyFilter


# API

class CurrencySerializer(serializers.ModelSerializer):

    class Meta:
        model = Currency
        fields = ('id', 'name', 'symbol', )


class CurrencyViewSet(viewsets.ModelViewSet):

    serializer_class = CurrencySerializer
    queryset = Currency.objects.all()
    lookup_field = 'id'
    filter_class = CurrencyFilter
