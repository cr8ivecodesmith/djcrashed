from django.db import models
from core.models import Base


class NoteBook(Base):
    title = models.CharField(max_length=512, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Label(Base):
    title = models.CharField(max_length=512, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Note(Base):
    title = models.CharField(max_length=512, blank=True)
    note = models.TextField(blank=True)
    notebook = models.ForeignKey(NoteBook, blank=True, null=True)
    labels = models.ManyToManyField(Label, blank=True)

    def __str__(self):
        return self.title
