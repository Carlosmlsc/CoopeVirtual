# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin
from .models import Entry, EntryDetail


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):

    list_display = ('id', 'entry_number', 'company', 'fiscal_period', 'date', 'cost_center', 'currency', 
                    'exchange_rate', 'status', 'typing_user', 'auth_user',)
    
    search_fields = ('id', 'entry_number', 'company', 'fiscal_period', 'date', 'cost_center', 'currency', 
                     'exchange_rate', 'status', 'typing_user', 'auth_user',)


@admin.register(EntryDetail)
class EntryDetailAdmin(admin.ModelAdmin):

    list_display = ('id',  'account', 'cash_flow', 'document', 'reference', 'credit', 'debit', 'balance', )

    search_fields = ('id', 'entry', 'account', 'cash_flow', 'document', 'reference', 'credit', 'debit', 'balance', )

    filter_horizontal = ('client', 'supplier')

