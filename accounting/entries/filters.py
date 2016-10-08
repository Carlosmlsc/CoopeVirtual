# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django_filters
from .models import Entry, EntryDetail


class EntryFilter(django_filters.FilterSet):

    class Meta:
        model = Entry
        fields = ('id', 'entry_number', 'company', 'fiscal_period', 'date', 'cost_center', 'currency', 'exchange_rate',
                  'status', 'typing_user', 'auth_user',)


class EntryDetailFilter(django_filters.FilterSet):

    class Meta:
        model = EntryDetail
        fields = ('id', 'entry', 'account', 'client', 'supplier', 'cash_flow', 'document', 'reference', 'credit',
                  'debit', 'balance', )
