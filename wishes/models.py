import os

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _


class Character(models.Model):

    class Meta:
        verbose_name = _('character')
        verbose_name_plural = _('characters')

    name = models.CharField(
        verbose_name=_('name'),
        max_length=255,
        db_index=True,
    )

    image = models.ImageField(
        verbose_name=_('image'),
        upload_to=os.path.join('wishes', 'character')
    )

    def __str__(self):
        return self.name


class Wish(models.Model):

    class Meta:
        verbose_name = _('wish')
        verbose_name_plural = _('wishes')

        ordering = ['-created']

    author = models.ForeignKey(
        verbose_name=_('author'),
        to=Character,
        on_delete=models.CASCADE,
    )

    text = models.TextField(
        verbose_name=_('text'),
    )

    created = models.DateTimeField(
        verbose_name=_('created at'),
        default=timezone.now
    )

    published = models.BooleanField(
        verbose_name=_('published'),
        default=False,
    )

    def __str__(self):
        return self.text