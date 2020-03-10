from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _
from isbn_field import ISBNField

User = get_user_model()


class Book(models.Model):
    name = models.CharField(_('Name'), max_length=255)
    isbn = ISBNField(_('ISBN'))
    publish_date = models.DateField(_('Date Created'))
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('Book')
        verbose_name_plural = _('Books')

    def __str__(self):
        return f'{self.name} {self.isbn} Author: {self.author}'
