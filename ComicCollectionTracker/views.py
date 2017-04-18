import urllib2
from xml.dom import minidom

import utils

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.views import View

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
    template_name = 'ComicCollectionTracker/issue.html'
    context_object_name = 'issue_object'

    def get_queryset(self):
        return Issue.objects.get(user=self.request.user)


@method_decorator(login_required, name='dispatch')
class ComicvineIssueView(View):

    def get(self, request):
        comicvine_id = request.GET.get('comicvine_id', '0')
        url = utils.get_comicvine_issue_url(comicvine_id)
        comicvine_content = urllib2.urlopen(url)
        xml_tree = minidom.parse(comicvine_content)
        comicvine_content.close()

        form = IssueAddForm(initial={
            'comicvine_id': comicvine_id,
            'comicvine_url': xml_tree.getElementsByTagName('site_detail_url')[0].firstChild.nodeValue,
            # 'publication',
            # 'number',
            # 'cover',
            # 'cover_url',
            # 'on_sale_date',
        })

        return render(request, 'ComicCollectionTracker/comicvine_issue.html',
                      {
                          'form': form
                      })
