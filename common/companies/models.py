# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Company(models.Model):

    commercial_name = models.CharField(max_length=100, null=True, verbose_name='Nombre Comercial')
    company_name = models.CharField(max_length=100, null=True, verbose_name='Razón Social')
    contact = models.CharField(max_length=100, null=True, verbose_name='Contacto')
    financial_id = models.DecimalField(max_digits=20, decimal_places=0, default=0, verbose_name='ID Fiscal')
    financial_accounting_id = models.DecimalField(max_digits=20, decimal_places=0, default=0,
                                                  verbose_name='ID Fiscal Contable')
    phone_numbers = models.ManyToManyField('CompanyPhoneNumber', blank=True, verbose_name='Números de teléfono')
    emails = models.ManyToManyField('CompanyEmail', blank=True, verbose_name='Emails')
    logo = models.ImageField(blank=True, null=True, verbose_name='Logo')
    slogan = models.CharField(max_length=255, blank=True, verbose_name='Eslogan')

    def __unicode__(self):
        return '%s' % self.comercial_name

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['id']


class CompanyPhoneNumber(models.Model):

    phone_number = models.DecimalField(max_digits=20, decimal_places=0, default=0, verbose_name='ID Fiscal')

    def __unicode__(self):
        return '%s' % self.phone_number

    class Meta:
        verbose_name = 'Teléfono'
        verbose_name_plural = 'Teléfonos'
        ordering = ['id']


class CompanyEmail(models.Model):

    email = models.EmailField(verbose_name='Email')

    def __unicode__(self):
        return '%s' % self.phone_number

    class Meta:
        verbose_name = 'Email'
        verbose_name_plural = 'Emails'
        ordering = ['id']
