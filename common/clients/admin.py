# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin
from .models import Client


@admin.register(Client)
class EntryAdmin(admin.ModelAdmin):

    list_display = ('id', 'company', 'name', 'last_name', 'code', 'id_type', 'id_num', 'address', 'phone', 'email', 'has_credit'
                    , 'credit_limit', 'debt', 'credit_days', )

    search_fields = ('id', 'company', 'name', 'code', 'last_name', 'id_type', 'id_num', 'address', 'phone', 'email',
                     'has_credit', 'credit_limit', 'debt', 'credit_days', )

