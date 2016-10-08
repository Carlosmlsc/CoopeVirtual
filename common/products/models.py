# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Product(models.Model):

    Unit = 'uni'
    Bulk = 'bul'
    Kit = 'kit'

    SELLS_CHOICES = ((Unit, 'Por Unidad'),
                     (Bulk, 'A Granel'),
                     (Kit, 'En Paquete(kit)'),
                     )

    code = models.PositiveIntegerField(verbose_name='Código', unique=True, default=0)
    barcode = models.PositiveIntegerField(verbose_name='Código de Barras', blank=True, default=0)
    description = models.CharField(max_length=255, verbose_name='Descripción del producto', default=' ')
    department = models.ForeignKey('ProductDepartment', on_delete=models.SET_NULL, null=True,
                                   verbose_name='Familia', default='')
    subdepartment = models.ForeignKey('ProductSubDepartment', on_delete=models.SET_NULL, null=True,
                                      verbose_name='Sub-Familia', default='')
    useinventory = models.BooleanField(default=False, verbose_name='Sistema de Inventarios?')
    inventory = models.FloatField(default=0, verbose_name='Existencia en Inventario')
    minimum = models.FloatField(default=0, verbose_name='Mínimo en inventario')
    sellmethod = models.CharField(max_length=3, choices=SELLS_CHOICES, default=Unit, verbose_name='Se Vende Por')
    cost = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name='Costo ₡')
    autoprice = models.BooleanField(default=False, verbose_name='Precio Automático?')
    utility = models.DecimalField(default=0, max_digits=5, decimal_places=2, verbose_name='Utilidad %')
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name='Precio sin Impuestos ₡')
    usetaxes = models.BooleanField(default=False, verbose_name='Usa Impuestos?')
    taxes = models.DecimalField(default=0, max_digits=4, decimal_places=2, verbose_name='Impuestos %')
    discount = models.DecimalField(default=0, max_digits=4, decimal_places=2, verbose_name='Descuento %')
    sellprice = models.DecimalField(default=0, max_digits=10, decimal_places=2, verbose_name='Precio de Venta ₡')

    def __unicode__(self):
        return '%s' % self.product_description

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['product_code']


class ProductDepartment(models.Model):

    name = models.CharField(max_length=255, verbose_name='Nombre de la Familia', unique=True)
    code = models.CharField(max_length=2, unique=True, verbose_name='Identificador de Familia')

    def __unicode__(self):
        return '%s' % self.productdepartment_name

    class Meta:
        verbose_name = 'Familia'
        verbose_name_plural = 'Familias'
        ordering = ['id']


class ProductSubDepartment(models.Model):

    department = models.ForeignKey('ProductDepartment', on_delete=models.SET_NULL, null=True, verbose_name='Familia')
    name = models.CharField(max_length=255, verbose_name='Nombre de la Sub-Familia', unique=True)
    code = models.CharField(max_length=2, verbose_name='Identificador de Sub-Familia')

    def __unicode__(self):
        return '%s' % self.productsubdepartment_name

    class Meta:
        verbose_name = 'Sub-Familia'
        verbose_name_plural = 'Sub-Familias'
        ordering = ['id']