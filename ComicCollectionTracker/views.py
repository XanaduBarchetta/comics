from django.shortcuts import render
from django.http import HttpResponse

from .models import User, Collection


def index(request):
    collection_list = Collection.objects.all()  # TODO: replace with real query
    context = {
        'collection_list': collection_list,
    }
    if not collection_list:
        return render(request, 'ComicCollectionTracker/create_collection_form.html', context)
