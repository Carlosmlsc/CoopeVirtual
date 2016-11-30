# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from common.companies.models import Company


class Product(models.Model):

    company = models.ForeignKey(Company, null=True, blank=True, verbose_name='Compañía')
    code = models.PositiveIntegerField(verbose_name='Código', default=0)
    description = models.CharField(max_length=255, verbose_name='Descripción del producto', null=True)
    department = models.ForeignKey('ProductDepartment', on_delete=models.SET_NULL, null=True,
                                   verbose_name='Familia', default='')
    subdepartment = models.ForeignKey('ProductSubDepartment', on_delete=models.SET_NULL, null=True,
                                      verbose_name='Sub-Familia', default='')
    useinventory = models.BooleanField(default=False, verbose_name='Sistema de Inventarios?')
    minimum = models.FloatField(default=0, verbose_name='Mínimo en inventario')
    unit = models.CharField(max_length=4, null=True, verbose_name='Unidad')
    cost = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name='Costo ₡')
    isactive = models.BooleanField(default=True, verbose_name='Activo?')
    hasforsale = models.BooleanField(default=False, verbose_name='Es para Venta?')

    def __unicode__(self):
        return '%s' % self.description

    class Meta:
        unique_together = ('company', 'code')
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['code']


class ProductForSale(models.Model):

    company = models.ForeignKey(Company, null=True, blank=True, verbose_name='Compañía')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Producto',
                                related_name='inventory_product')
    code = models.PositiveIntegerField(verbose_name='Código', default=0)
    barcode = models.PositiveIntegerField(verbose_name='Código de Barras', blank=True, default=0)
    description = models.CharField(max_length=255, verbose_name='Descripción del producto', null=True)
    department = models.ForeignKey('ProductDepartment', on_delete=models.SET_NULL, null=True,
                                   verbose_name='Familia', default='')
    subdepartment = models.ForeignKey('ProductSubDepartment', on_delete=models.SET_NULL, null=True,
                                      verbose_name='Sub-Familia', default='')
    unit = models.CharField(max_length=4, null=True, verbose_name='Unidad')
    utility = models.DecimalField(default=0, max_digits=5, decimal_places=2, verbose_name='Utilidad %')
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name='Precio sin Impuestos ₡')
    usetaxes = models.BooleanField(default=False, verbose_name='Usa Impuestos?')
    taxes = models.DecimalField(default=0, max_digits=4, decimal_places=2, verbose_name='Impuestos %')
    discount = models.DecimalField(default=0, max_digits=4, decimal_places=2, verbose_name='Descuento %')
    sellprice = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name='Precio de Venta ₡')
    isactive = models.BooleanField(default=True, verbose_name='Activo?')
    iscomposed = models.BooleanField(default=False, verbose_name='Es Compuesto?')

    def __unicode__(self):
        return '%s' % self.description

    class Meta:
        unique_together = (('company', 'code'), ('company', 'barcode'))
        verbose_name = 'Producto para la Venta'
        verbose_name_plural = 'Productos para la Venta'
        ordering = ['code']


class ProductDepartment(models.Model):

    company = models.ForeignKey(Company, null=True, verbose_name='Compañía')
    name = models.CharField(max_length=255, verbose_name='Nombre de la Familia')
    code = models.CharField(max_length=2, verbose_name='Identificador de Familia')

    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        unique_together = (('company', 'code'), ('company', 'name'))
        verbose_name = 'Familia'
        verbose_name_plural = 'Familias'
        ordering = ['id']


class ProductSubDepartment(models.Model):

    department = models.ForeignKey('ProductDepartment', on_delete=models.SET_NULL, null=True, verbose_name='Familia')
    name = models.CharField(max_length=255, verbose_name='Nombre de la Sub-Familia')
    code = models.CharField(max_length=2, verbose_name='Identificador de Sub-Familia')

    def __unicode__(self):
        return '%s' % self.name

    class Meta:
        unique_together = (('department', 'code'), ('department', 'name'))
        verbose_name = 'Sub-Familia'
        verbose_name_plural = 'Sub-Familias'
        ordering = ['id']


