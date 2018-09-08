# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from model_utils.models import TimeStampedModel

# Create your models here.
class BaseModel(TimeStampedModel):
	pass

	class Meta:
		abstract = True


class CatalogModel(BaseModel):
	name = models.CharField(verbose_name='Nombre', max_length=255)
	display_name = models.CharField(verbose_name='Nombre a visualizar', max_length=255)

	class Meta:
		abstract = True

	def __unicode__(self):
		return u'{}'.format(self.display_name)


class StateMx(models.Model):
    key_state = models.CharField(max_length=5)
    name = models.CharField(max_length=255, verbose_name='nombre')

    def __unicode__(self):
        return '{}'.format(self.name)


class MunicipalityMx(models.Model):
    key_municipality = models.CharField(max_length=5)
    state = models.ForeignKey(StateMx, verbose_name='estado', related_name='municipalities')
    name = models.CharField(max_length=255, verbose_name='nombre')

    def __unicode__(self):
        return '{}'.format(self.name)


class LocalityMx(models.Model):
    key_locality = models.CharField(max_length=5)
    municipality = models.ForeignKey(MunicipalityMx, verbose_name='municipio', related_name='municipalities')
    name = models.CharField(max_length=255, verbose_name='nombre')

    def __unicode__(self):
        return '{}'.format(self.name)
