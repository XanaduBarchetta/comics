from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView

from .models import Issue


@method_decorator(login_required, name='dispatch')
class IssueList(ListView):
    template_name = 'ComicCollectionTracker/index.html'
    context_object_name = 'issues'

    def get_queryset(self):
        return Issue.objects.filter(user=self.request.user)
