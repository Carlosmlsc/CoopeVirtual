# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers, viewsets
from .models import Account
from .filters import AccountFilter


# API

class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('id', 'description', )


class AccountViewSet(viewsets.ModelViewSet):

    serializer_class = AccountSerializer
    queryset = Account.objects.all()
    lookup_field = 'id'
    filter_class = AccountFilter
