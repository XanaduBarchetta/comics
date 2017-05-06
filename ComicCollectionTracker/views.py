# Python libraries
import urllib2
import json
import logging

# Project libraries
import utils

# Django libraries
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.views import View

# Models and forms
from .models import Issue
from .forms import ComicvineIssueForm, IssueAddForm


@method_decorator(login_required, name='dispatch')
class IssueListView(ListView):
    template_name = 'ComicCollectionTracker/index.html'
    context_object_name = 'issues_list'
    form_issue = ComicvineIssueForm()

    def get_queryset(self):
        return Issue.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(IssueListView, self).get_context_data(**kwargs)
        context['form_issue'] = self.form_issue
        return context


@method_decorator(login_required, name='dispatch')
class IssueDetailView(DetailView):
    template_name = 'ComicCollectionTracker/issue_detail.html'
    context_object_name = 'issue_object'
    model = Issue

    def get_queryset(self):
        queryset = super(IssueDetailView, self).get_queryset()
        # Filter the queryset to make sure the requested Issue actually belongs to the requesting User
        return queryset.filter(user=self.request.user)


@method_decorator(login_required, name='dispatch')
class ComicvineIssueView(View):

    def get(self, request):
        comicvine_id = request.GET.get('comicvine_id', '0')
        url = utils.get_comicvine_issue_url(comicvine_id)
        logger = logging.getLogger(settings.LOGGER_NAME)
        logger.info("Making API call to url [" + url + "]")
        comicvine_content = urllib2.urlopen(url)
        comic_data = json.loads(comicvine_content.read())
        comicvine_content.close()

        # TODO: Handle errors

        # Create dictionary from JSON

        form = IssueAddForm(initial={
            'comicvine_id': comicvine_id,
            'comicvine_url': comic_data['results']['site_detail_url'],
            'publication': comic_data['results']['volume']['name'],
            'number': comic_data['results']['issue_number'],
            'cover_url': comic_data['results']['image']['small_url'],
            'on_sale_date': comic_data['results']['store_date'],
        })

        return render(request, 'ComicCollectionTracker/comicvine_issue.html',
                      {
                          'form': form
                      })

    def post(self, request):
        form = IssueAddForm(request.POST)
        if form.is_valid():
            new_issue = form.save(commit=False)
            new_issue.user = request.user  # Attach this new issue to the current user
            new_issue.save()
            return HttpResponseRedirect(reverse('collection-index'))
        else:
            return render(request, 'ComicCollectionTracker/comicvine_issue.html',
                          {
                              'form': form
                          })
