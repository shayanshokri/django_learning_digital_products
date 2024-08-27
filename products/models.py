from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name=_('Parent'), blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_('Title'), max_length=50)
    description = models.TextField(verbose_name=_('Description'), blank=True)
    avatar = models.ImageField(verbose_name=_('Avatar'), blank=True, upload_to='categories')
    active = models.BooleanField(verbose_name=_('Active'), default=True)
    created_time = models.DateTimeField(verbose_name=_('Created Time'), auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name=_('Updated Time'), auto_now=True)

    class Meta:
        db_table = 'categories'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Product(models.Model):
    category = models.ManyToManyField('Category', verbose_name=_('Category'), blank=True)
    title = models.CharField(verbose_name=_('Title'), max_length=50)
    description = models.TextField(verbose_name=_('Description'), blank=True)
    avatar = models.ImageField(verbose_name=_('Avatar'), blank=True, upload_to='categories/')
    active = models.BooleanField(verbose_name=_('Active'), default=True)
    created_time = models.DateTimeField(verbose_name=_('Created Time'), auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name=_('Updated Time'), auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class File(models.Model):
    product = models.ForeignKey('Product', verbose_name=_('Product'), on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_('Title'), max_length=50)
    file = models.FileField(verbose_name=_('File'), upload_to='files/%Y/%m/%d')
    active = models.BooleanField(verbose_name=_('Active'), default=True)
    created_time = models.DateTimeField(verbose_name=_('Created Time'), auto_now_add=True)
    updated_time = models.DateTimeField(verbose_name=_('Updated Time'), auto_now=True)

    class Meta:
        db_table = 'files'
        verbose_name = _('File')
        verbose_name_plural = _('Files')
