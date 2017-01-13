from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

from .models import Collection, Issue


@login_required
def index(request):
    if Collection.objects.filter(user=request.user, is_default=True).exists():
        # Prompt the user to create their first collection
        return render(request, 'ComicCollectionTracker/create_collection_form.html')
    else:
        return render(request, 'ComicCollectionTracker/index.html')


@login_required
class IssueList(ListView):
    model = Issue
