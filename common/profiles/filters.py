# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django_filters
from django.contrib.auth.models import User
from .models import Profile


class UserFilter(django_filters.FilterSet):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'groups', 'user_permissions',
                  'is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined')


class ProfileFilter(django_filters.FilterSet):

    class Meta:
        model = Profile
        fields = ('id', 'user', 'company', 'is_admin', 'is_premium',)
