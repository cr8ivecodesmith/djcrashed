from django.db import models


class Base(models.Model):
    """Base abstract model that provides common audit fields

    All app models should inherit this model

    """
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    active = models.BooleanField(default=True)

    class Meta:
        abstract = True
