# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django_filters
from .models import Account


class AccountFilter(django_filters.FilterSet):

    class Meta:
        model = Account
        fields = ('id', 'description', )
