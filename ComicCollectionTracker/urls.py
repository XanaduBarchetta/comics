from django.conf.urls import url

from ComicCollectionTracker.views import IssueList


urlpatterns = [
    url(r'^$', IssueList, name='collection'),
]
