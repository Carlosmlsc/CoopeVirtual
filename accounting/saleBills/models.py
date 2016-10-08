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
    sub_total = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Subtotal')
    discount = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Descuento')
    exempt = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Excento')
    with_tax = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Gravado')
    tax_amount = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Impuestos')
    total = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Total')

    def __unicode__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Factura de Venta'
        verbose_name_plural = 'Facturas de Venta'
        ordering = ['id']


class SaleBillDetail(models.Model):

    sale_bill = models.ForeignKey('SaleBill', verbose_name='Factura de Venta')
    product_code = models.PositiveIntegerField(verbose_name='Código del producto')
    qty = models.PositiveIntegerField(verbose_name='Cantidad')
    description = models.CharField(max_length=255, verbose_name='Descripción')
    use_taxes = models.BooleanField(default=False, verbose_name='Excento o Gravado?')
    tax_percentage = models.FloatField(verbose_name='Porcentaje de Impuestos')
    unit_price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Precio Unitario')
    subtotal = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Subtotal')

    def __unicode__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Detalle de Factura'
        verbose_name_plural = 'Detalles de Factura'
        ordering = ['id']