# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from common.companies.models import Company
from common.currencies.models import Currency
from common.clients.models import Client


class SaleBill(models.Model):

    company = models.ForeignKey(Company, verbose_name='Empresa')
    sale_num = models.PositiveIntegerField(verbose_name='Consecutivo')
    date = models.DateField(verbose_name='Fecha')
    currency = models.ForeignKey(Currency, verbose_name='Moneda')
    client = models.ForeignKey(Client, verbose_name='Cliente')

    def __unicode__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Factura de Venta'
        verbose_name_plural = 'Facturas de Venta'
        ordering = ['id']


class SaleBillDetail(models.Model):

    sale_bill = models.ForeignKey('SaleBill', verbose_name='Factura de Venta')

    def __unicode__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Detalle de Factura'
        verbose_name_plural = 'Detalles de Factura'
        ordering = ['id']