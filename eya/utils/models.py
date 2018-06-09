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
		return u'{}'.format(display_name)