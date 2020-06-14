import os

from django.db import models
from django.utils.translation import ugettext_lazy as _
from mptt.models import MPTTModel


class Slide(MPTTModel):

    class Meta:
        verbose_name = _('slide')
        verbose_name_plural = _('slides')

        ordering = ['lft']

    title = models.CharField(
        verbose_name=_('title'),
        max_length=255,
    )

    image = models.ImageField(
        verbose_name=_('image'),
        upload_to=os.path.join('slides', 'slide'),
    )

    text = models.TextField(
        blank=True,
        null=True,
    )

    published = models.BooleanField(
        verbose_name=_('published'),
        default=False,
    )

    def __str__(self):
        return self.title
