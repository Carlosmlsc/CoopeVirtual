# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from accounting.fiscalPeriods.models import FiscalPeriod
from accounting.accounts.models import Account
from common.clients.models import Client
from common.companies.models import Company
from common.currencies.models import Currency
from common.suppliers.models import Supplier


class Entry(models.Model):

    entry_number = models.PositiveIntegerField(verbose_name='Consecutivo')
    company = models.ForeignKey(Company, verbose_name='Empresa')
    fiscal_period = models.ForeignKey(FiscalPeriod, verbose_name='Periodo Fiscal')  # todo Automatico?
    date = models.DateField(verbose_name='Fecha')
    cost_center = models.PositiveIntegerField(verbose_name='Centro de Costos')
    currency = models.ForeignKey(Currency, verbose_name='Moneda')
    exchange_rate = models.DecimalField(max_digits=10, decimal_places=6, verbose_name='Tipo de Cambio')
    status = models.CharField(max_length=255, verbose_name='Estado')  # todo Modelo o predeterminado?
    typing_user = models.PositiveIntegerField(verbose_name='Registrador')
    auth_user = models.PositiveIntegerField(verbose_name='Integrador')

    def __unicode__(self):
        return '%s' % self.comercial_name

    class Meta:
        verbose_name = 'Asiento'
        verbose_name_plural = 'Asientos'
        ordering = ['id']


class EntryDetail(models.Model):

    # todo tipo? para ver si es cliente o proveedor?
    entry = models.ForeignKey('Entry', verbose_name='Asiento')
    account = models.ForeignKey(Account, verbose_name='Cuenta')
    # todo date for detail
    client = models.ManyToManyField(Client, blank=True, verbose_name='Cliente')
    supplier = models.ManyToManyField(Supplier, blank=True, verbose_name='Proveedor')
    cash_flow = models.CharField(max_length=255, verbose_name='Flujo de Caja')
    document = models.PositiveIntegerField(verbose_name='Documento')  # todo agregar link en el frontend char
    reference = models.PositiveIntegerField(verbose_name='Referencia')  # todo agregar link en el frontend char
    credit = models.FloatField(verbose_name='Debe')
    debit = models.FloatField(verbose_name='Haber')
    balance = models.FloatField(verbose_name='Diferencia')

    def __unicode__(self):
        return '%s' % self.id

    class Meta:
        verbose_name = 'Detalle de Asiento'
        verbose_name_plural = 'Detalles de Asiento'
        ordering = ['id']

