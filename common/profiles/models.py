# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from common.companies.models import Company

from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, null=True, verbose_name='Compañía')
    is_admin = models.BooleanField(default=False, verbose_name='Es Admin?')
    is_premium = models.BooleanField(default=False, verbose_name='Es Premium?')

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    # @receiver(post_save, sender=User)
    # def ensure_profile_exists(sender, **kwargs):
    #     if kwargs.get('created', False):
    #         Profile.objects.get_or_create(user=kwargs.get('instance'))
    #     if not Profile.objects.filter(user=kwargs.get('instance')):
    #         Profile.objects.get_or_create(user=kwargs.get('instance'))

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __unicode__(self):
        return '%s' % self.user.first_name

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'
        ordering = ['id']
