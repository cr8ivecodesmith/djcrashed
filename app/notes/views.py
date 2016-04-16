import pdb

from django.db.models import Q
from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View

from .models import Note


class Index(View):
    """
    https://docs.djangoproject.com/en/1.9/topics/class-based-views/intro/
    """
    template_name = 'notes/index.html'

    def get_context_data(self, **kwargs):
        context = {}
        notes = Note.objects.all()

        context['note_list'] = notes

        context.update(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)
