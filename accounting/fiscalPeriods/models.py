# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class FiscalPeriod(models.Model):

    description = models.CharField(max_length=255, verbose_name='Periodo Fiscal')
    # todo start date y end date
    # todo activo?

    def __unicode__(self):
        return '%s' % self.description

    class Meta:
        verbose_name = 'Periodo Fiscal'
        verbose_name_plural = 'Periodos Fiscales'
        ordering = ['id']
