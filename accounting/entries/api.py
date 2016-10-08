# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers, viewsets
from .models import Entry, EntryDetail
from .filters import EntryFilter, EntryDetailFilter


# API

class EntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Entry
        fields = ('id', 'entry_number', 'company', 'fiscal_period', 'date', 'cost_center', 'currency', 'exchange_rate',
                  'status', 'typing_user', 'auth_user',)


class EntryViewSet(viewsets.ModelViewSet):

    serializer_class = EntrySerializer
    queryset = Entry.objects.all()
    lookup_field = 'id'
    filter_class = EntryFilter


# API

class EntryDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = EntryDetail
        fields = ('id', 'entry', 'account', 'client', 'supplier', 'cash_flow', 'document', 'reference', 'credit',
                  'debit', 'balance', )


class EntryDetailViewSet(viewsets.ModelViewSet):

    serializer_class = EntryDetailSerializer
    queryset = EntryDetail.objects.all()
    lookup_field = 'id'
    filter_class = EntryDetailFilter