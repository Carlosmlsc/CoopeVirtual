# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers, viewsets
from django.contrib.auth.models import User
from .models import Profile
from .filters import ProfileFilter, UserFilter


# API

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'groups', 'user_permissions',
                  'is_staff', 'is_active', 'is_superuser', 'last_login', 'date_joined')


class UserViewSet(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'username'
    filter_class = UserFilter


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = ('id', 'user', 'company', 'is_admin', 'is_premium',)


class ProfileViewSet(viewsets.ModelViewSet):

    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    lookup_field = 'user'
    filter_class = ProfileFilter