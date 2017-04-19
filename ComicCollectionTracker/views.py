import urllib2
from xml.dom import minidom
import json

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
        comic_data = json.loads(comicvine_content.read())
        comicvine_content.close()

        # TODO: Handle errors

        # Create dictionary from JSON

        form = IssueAddForm(initial={
            'comicvine_id': comicvine_id,
            'comicvine_url': comic_data['results']['site_detail_url'],
            'publication': comic_data['results']['volume']['name'],
            'number': comic_data['results']['issue_number'],
            'cover_url': comic_data['results']['image']['super_url'],
            'on_sale_date': comic_data['results']['store_date'],
        })

        return render(request, 'ComicCollectionTracker/comicvine_issue.html',
                      {
                          'form': form
                      })
# {
#     "error":"OK",
#     "limit":1,
#     "offset":0,
#     "number_of_page_results":1,
#     "number_of_total_results":1,
#     "status_code":1,
#     "results":{
#         "image":{
#             "icon_url":"https:\/\/comicvine.gamespot.com\/api\/image\/square_avatar\/2556504-smann_cv1.jpeg",
#             "medium_url":"https:\/\/comicvine.gamespot.com\/api\/image\/scale_medium\/2556504-smann_cv1.jpeg",
#             "screen_url":"https:\/\/comicvine.gamespot.com\/api\/image\/screen_medium\/2556504-smann_cv1.jpeg",
#             "small_url":"https:\/\/comicvine.gamespot.com\/api\/image\/scale_small\/2556504-smann_cv1.jpeg",
#             "super_url":"https:\/\/comicvine.gamespot.com\/api\/image\/scale_large\/2556504-smann_cv1.jpeg",
#             "thumb_url":"https:\/\/comicvine.gamespot.com\/api\/image\/scale_avatar\/2556504-smann_cv1.jpeg",
#             "tiny_url":"https:\/\/comicvine.gamespot.com\/api\/image\/square_mini\/2556504-smann_cv1.jpeg"
#         },
#         "issue_number":"1",
#         "site_detail_url":"https:\/\/comicvine.gamespot.com\/superman-annual-1-alien-extinction\/4000-354034\/",
#         "volume":{
#             "api_detail_url":"https:\/\/comicvine.gamespot.com\/api\/volume\/4050-51617\/",
#             "id":51617,
#             "name":"Superman Annual",
#             "site_detail_url":"https:\/\/comicvine.gamespot.com\/superman-annual\/4050-51617\/"
#         }
#     },
#     "version":"1.0"
# }
