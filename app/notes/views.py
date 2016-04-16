from django.db.models import Q
from django.http import Http404
from django.shortcuts import render
from django.views.generic import View

from .models import Note


class Index(View):
    """
    https://docs.djangoproject.com/en/1.9/topics/class-based-views/intro/
    """
    template_name = 'notes/index.html'

    def get_context_data(self, **kwargs):
        context = {}
        q = self.request.GET.get('q')
        notes = Note.objects
        if q:
            notes = notes.filter(Q(title__icontains=q)|Q(note__icontains=q))
        else:
            notes = notes.all()

        context['note_list'] = notes

        context.update(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        new_note = request.POST.get('txtNewNote')

        if new_note:
            Note.objects.create(note=new_note)

        return render(request, self.template_name, context)
