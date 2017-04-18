from django import forms

from django.contrib.auth.models import User

from .models import Issue


class ComicvineIssueForm(forms.Form):
    comicvine_id = forms.IntegerField(label='Comicvine ID: 4000-', label_suffix='')


class IssueAddForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = [
            'comicvine_id',
            'comicvine_url',
            'publication',
            'number',
            'printing',
            'cover',
            'cover_url',
            'on_sale_date',
            'issue_comment',
            'own_physical',
            'own_digital',
            'have_read',
            'collection_comment',
        ]
    
    def __init__(self, *args, **kwargs):
        super(IssueAddForm, self).__init__(*args, **kwargs)
        self.fields['comicvine_url'].widget.attrs['size'] = 100
