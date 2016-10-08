# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin
from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):

    list_display = ('id', 'commercial_name', 'company_name', 'contact', 'financial_id', 'financial_accounting_id',
                    'slogan',)

    search_fields = ('id', 'commercial_name', 'company_name', 'contact', 'financial_id', 'financial_accounting_id',
                     'phone_numbers', 'emails', 'slogan',)
