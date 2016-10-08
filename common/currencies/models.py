# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Currency(models.Model):

    name = models.CharField(max_length=255, verbose_name='Moneda')
    symbol = models.CharField(max_length=3, verbose_name='Símbolo')

    def __unicode__(self):
        return '%s' % self.symbol

    class Meta:
        verbose_name = 'Moneda'
        verbose_name_plural = 'Monedas'
        ordering = ['id']

