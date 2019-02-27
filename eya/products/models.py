# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from random import randint

from django.db import models
from django.db.models import Q

from imagekit.models import ProcessedImageField
from imagekit.processors import SmartResize
from utils.models import BaseModel, CatalogModel


def get_image_path(instance, filename):
    ext = filename.decode('utf-8').split('.')[-1]
    return 'product/{0}/{1}.{2}'.format(instance.code_eyamex, instance.code_eyamex, ext)


# Create your models here.
class Type(CatalogModel):
    pass

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'


class Clasification(CatalogModel):
    pass

    class Meta:
        verbose_name = u'Clasificación'
        verbose_name_plural = u'Clasificaciones'


class Color(CatalogModel):
    pass

    class Meta:
        verbose_name = 'Color'
        verbose_name_plural = 'Colores'

    def __unicode__(self):
        return u'{}-{}'.format(self.name, self.display_name)


class Family(BaseModel):
    description = models.TextField(verbose_name=u'Descripción')

    class Meta:
        verbose_name = 'Familia'
        verbose_name_plural = 'Familias'

    def __unicode__(self):
        return u'{}'.format(self.description)


class Product(BaseModel):
    code_eyamex = models.CharField(verbose_name=u'Código EYAMEX', max_length=20)
    image = ProcessedImageField(
        upload_to=get_image_path, format='JPEG',
        processors=[SmartResize(994, 660)], options={'quality': 100},
        verbose_name=u"Imagen", null=True)
    family = models.ForeignKey(Family, verbose_name='Familia', related_name='f_products', null=True)
    type = models.ForeignKey(Type, verbose_name='Tipo', related_name='t_products', null=True)
    clasification = models.ForeignKey(Clasification, verbose_name=u'Clasificación', related_name='c_products')
    code = models.CharField(verbose_name=u'Código', max_length=15)
    color = models.ForeignKey(Color, verbose_name='Color', related_name='cl_products')
    description = models.CharField(verbose_name=u'Descripción', max_length=255)
    meta_description = models.TextField()
    is_new = models.BooleanField(verbose_name='¿Es nuevo?', default=False)
    home_is_new = models.BooleanField(verbose_name='¿Es nuevo aparece en banner?', default=False)
    best_seller = models.BooleanField(verbose_name=u'¿Más vendido?')
    home_best_seller = models.BooleanField(verbose_name=u'¿Más vendido aparece en banner?', default=False)
    spent = models.BooleanField(verbose_name='¿Agotado?')
    quantity = models.DecimalField(verbose_name='Cantidad', max_digits=10, decimal_places=2, default=0)
    quantity_descr = models.CharField(verbose_name=u'Cantidad descripción', max_length=200)
    category = models.CharField(verbose_name=u'Categoria', max_length=200)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __unicode__(self):
        return u'{}'.format(self.code_eyamex)

    def fill_meta(self):
        meta_description = u'{} {} {} {} {} {} {} {}'.format(
            self.code_eyamex, self.clasification.name,
            self.code, self.color.name, self.description, self.family.description,
            self.quantity_descr, self.category)
        return meta_description.lower()

    def save(self, *args, **kwargs):
        self.meta_description = self.fill_meta()
        super(Product, self).save(*args, **kwargs)

    def get_products_related(self):
        ids = list()
        size = 0
        related = Product.objects.filter(
            family=self.family,
            clasification=self.clasification).exclude(Q(pk=self.pk) | Q(spent=True))
        if len(related) >= 4 :
            while size < 4:
                index = randint(0, len(related) - 1)
                prd = related[index]
                if prd.pk not in ids:
                    ids.append(prd.pk)
                size = len(ids)
            return related.filter(id__in=ids)
        return related
