from typing import List
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import Http404
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Note
from .forms import NotesForm

class NotesDeleteView(DeleteView):
    model = Note
    success_url = '/smart/notes'
    context_object_name = 'note'

class NotesUpdateView(UpdateView):
    model = Note
    success_url = '/smart/notes'
    form_class = NotesForm


class NotesCreateView(CreateView):
    model = Note
    success_url = '/smart/notes'
    form_class = NotesForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
    

class NotesListView(LoginRequiredMixin, ListView):
    model = Note
    context_object_name = 'notes'
    login_url = '/admin'

    def get_queryset(self) :
        return self.request.user.note.all()

# def list(request):
#     all_notes = Note.objects.all()
#     return render(request, './notes/notes_list.html',{'notes':all_notes})

class NotesDetailView(DetailView):
    model = Note
    context_object_name = 'note'

def details(request, pk):
    try:
        note = Note.objects.get(id=pk)
    except Note.DoesNotExist:
        raise Http404("Note does not exist")
    return render(request, './notes/notes_details.html', {'note':note})


