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


class NoteUpdate(View):
    template_name = 'notes/note_update.html'

    def get_context_data(self, **kwargs):
        context = {}
        try:
            note_id = kwargs.get('pk')
            note = Note.objects.get(id=note_id)
            context['note'] = note
        except Note.DoesNotExist:
            raise Http404

        context.update(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        note = context.get('note')
        note_title = request.POST.get('txtNoteTitle', '').strip()
        note_note = request.POST.get('txtNoteNote', '').strip()
        note.title = note_title
        note.note = note_note
        note.save()
        return render(request, self.template_name, context)


class NoteDelete(NoteUpdate):
    template_name = 'notes/note_delete.html'

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        note = context.get('note')
        note.delete()
        return redirect('notes:index')
