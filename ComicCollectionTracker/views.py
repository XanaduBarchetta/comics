from django.conf import settings

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView

from .models import Issue


@method_decorator(login_required, name='dispatch')
class IssueList(ListView):
    template_name = 'ComicCollectionTracker/index.html'
    context_object_name = 'issues_list'

    def get_queryset(self):
        return Issue.objects.filter(user=self.request.user)


@method_decorator(login_required, name='dispatch')
class IssueDetail(DetailView):
    template_name = 'ComicCollectionTracker/issue.html'
    context_object_name = 'issue_object'

    def get_queryset(self):
        return Issue.objects.get(user=self.request.user)
