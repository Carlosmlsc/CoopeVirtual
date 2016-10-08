# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin
from .models import Currency


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'symbol', )

    search_fields = ('id', 'name', 'symbol', )
