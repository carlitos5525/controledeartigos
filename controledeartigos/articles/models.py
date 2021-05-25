from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
from django.db.models.fields import CharField


class Article(models.Model):
    STATUS_CHOICES = (
        ('AF', 'A fazer'),
        ('FF', 'Feito'),
        ('AR', 'Atualizar'),
        ('AO', 'Atualizado')
    )

    PRODUCT_CHOICES = (
        ('CE', 'Celero'),
        ('ST', 'Start'),
        ('FW', 'Flow')
    )

    name = models.CharField(max_length=150)
    url = models.URLField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
    last_updated = models.DateField(auto_now=True)
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    category = models.CharField(max_length=150, null=True, blank=True)
    product = models.CharField(max_length=2, choices=PRODUCT_CHOICES)
    is_deleted = models.BooleanField(default=False)
