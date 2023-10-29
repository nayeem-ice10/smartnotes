from django import forms
from .models import Note
from django.core.exceptions import ValidationError

class NotesForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'text')
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'text' : forms.TextInput(attrs={'class':'form-control'})
        }

        labels = {
            'title': 'Your Notes Title is here:',
            'text': 'Write your Thoughts here:',
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if 'Django' not in title:
            raise ValidationError("We only accept notes about Django!")
        return title