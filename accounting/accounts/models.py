# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Account(models.Model):

    description = models.CharField(max_length=255, verbose_name='Descripción')
    # compañia
    #
    def __unicode__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Cuenta'
        verbose_name_plural = 'Cuentas'
        ordering = ['id']

# grupo de cuentas




# sub grupo de cuentas