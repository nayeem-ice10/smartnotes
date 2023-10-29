from django.shortcuts import render
from django.http import Http404
from django.views.generic import CreateView, ListView, DetailView
# Create your views here.
from .models import Note
from .forms import NotesForm


class NotesCreateView(CreateView):
    model = Note
    # fields = ['title', 'text']
    success_url = '/smart/notes'
    form_class = NotesForm
    

class NotesListView(ListView):
    model = Note
    context_object_name = 'notes'

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


