# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Supplier(models.Model):

    name = models.CharField(max_length=255, verbose_name='Nombre')

    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedor'
        ordering = ['id']
