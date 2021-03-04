from django.db import models
from django.db.models import Manager
from django.utils.translation import gettext_lazy as _


class Book(models.Model):
    title = models.CharField(
        verbose_name=_('title'), help_text=_('title'),
        max_length=32
    )
    description = models.CharField(
        verbose_name=_('description'), help_text=_('description'),
        max_length=200, default=''
    )
    author = models.CharField(
        verbose_name=_('author'), help_text=_('author'),
        max_length=32, default=''
    )
    genre = models.CharField(
        verbose_name=_('genre'), help_text=_('genre'),
        max_length=32, default=''
    )
    rating = models.DecimalField(
        verbose_name=_('rating'), help_text=_('rating'),
        default=0, decimal_places=1, max_digits=1
    )
    image = models.FileField(blank=True, upload_to='photos/%d-%m-%Y')
    created = models.DateTimeField(
        verbose_name=_('created'), help_text=_('created'),
        auto_now_add=True,
    )
    release_date = models.DateTimeField(
        verbose_name=_('release_date'), help_text=_('release_date'),
    )
    isbn = models.CharField(
        verbose_name=_('isbn'), help_text=_('isbn'),
        max_length=32, default=''
    )
    quantity = models.IntegerField(
        verbose_name=_('quantity'), help_text=_('quantity'),
        default=0
    )
    language = models.CharField(
        verbose_name=_('isbn'), help_text=_('isbn'),
        max_length=32, default='russian'
    )

    objects: Manager

    class Meta:
        app_label = 'books'
        db_table = 'books.books'
        verbose_name = _('book')
        verbose_name_plural = _('books')
