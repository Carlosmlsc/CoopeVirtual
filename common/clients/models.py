# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Client(models.Model):

    person = 'per'
    juridic = 'jur'
    passport = 'pas'

    ID_TYPE_CHOICES = ((person, 'Cédula Física'),
                     (juridic, 'Cédula Jurídica'),
                     (passport, 'Pasaporte'),
                     )

    name = models.CharField(max_length=255, verbose_name='Nombre')
    last_name = models.CharField(max_length=255, null=True, blank=True)
    id_type = models.CharField(max_length=3, choices=ID_TYPE_CHOICES, default=person, verbose_name='Tipo de Identificación')
    id = models.CharField(max_length=255, null=True, blank=True, verbose_name='Num Identificación')
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name='Dirección')
    phone = models.CharField(max_length=20, null=True, blank=True, verbose_name='Teléfono')
    email = models.EmailField(null=True, blank=True, verbose_name='Email')
    has_credit = models.BooleanField(default=False, verbose_name='Tiene Crédito?')
    credit_limit = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Límite de Crédito', null=True, blank=True)
    debt = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Saldo', null=True, blank=True)
    credit_days = models.PositiveIntegerField(default=30, null=True, blank=True, verbose_name='Días de Crédito')

    def __unicode__(self):
        return '%s %s' % (self.client_name, self.client_last_name)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']

