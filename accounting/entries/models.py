# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from common.companies.models import Company
from django.contrib.auth.models import User

# Create your models here.


class Entry(models.Model):

    entry_number = models.PositiveIntegerField(verbose_name='Consecutivo')
    company = models.ForeignKey(Company, verbose_name='Empresa')

    date = models.DateField(verbose_name='Fecha')
    cost_center = models.PositiveIntegerField(verbose_name='Centro de Costos')
    typing_user = models.ForeignKey(User, 'Registrador')
    auth_user = models.ForeignKey(User, 'Integrador')



