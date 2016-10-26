# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('id', 'user', 'company', 'is_admin', 'is_premium',)

    search_fields = ('id', 'user', 'company', 'is_admin', 'is_premium',)

