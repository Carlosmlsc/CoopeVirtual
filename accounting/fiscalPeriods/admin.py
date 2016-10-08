# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin
from .models import FiscalPeriod


@admin.register(FiscalPeriod)
class FiscalPeriodAdmin(admin.ModelAdmin):

    list_display = ('id', 'description',)

    search_fields = ('id', 'description',)
