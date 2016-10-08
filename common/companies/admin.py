# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin
from .models import Company, CompanyEmail, CompanyPhoneNumber


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):

    list_display = ('id', 'commercial_name', 'company_name', 'contact', 'financial_id', 'financial_accounting_id',
                    'slogan',)

    search_fields = ('id', 'commercial_name', 'company_name', 'contact', 'financial_id', 'financial_accounting_id',
                     'phone_numbers', 'emails', 'slogan',)

    filter_horizontal = ('phone_numbers', 'emails')


@admin.register(CompanyEmail)
class CompanyEmailAdmin(admin.ModelAdmin):

    list_display = ('id', 'email',)

    search_fields = ('id', 'email',)


@admin.register(CompanyPhoneNumber)
class CompanyPhoneNumberAdmin(admin.ModelAdmin):

    list_display = ('id', 'phone_number',)

    search_fields = ('id', 'phone_number',)
