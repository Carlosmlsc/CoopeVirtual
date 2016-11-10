# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from common.companies.models import Company


class InventoryMovement(models.Model):

    company = models.ForeignKey(Company, null=True, verbose_name='Compañía')
