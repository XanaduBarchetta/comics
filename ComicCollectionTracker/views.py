from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

from .models import Issue


@login_required
def IssueList(request):
    return render(request, 'ComicCollectionTracker/index.html')
