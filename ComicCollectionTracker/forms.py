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

        # Change widget sizes
        # TODO: maybe handle these things with javascript?
        self.fields['comicvine_url'].widget.attrs['size'] = 100
        self.fields['publication'].widget.attrs['size'] = 50
        self.fields['printing'].widget.attrs['size'] = 4
        self.fields['cover'].widget.attrs['size'] = 4
        self.fields['cover_url'].widget.attrs['size'] = 100

        # Change required fields
        self.fields['issue_comment'].required = False
        self.fields['collection_comment'].required = False
