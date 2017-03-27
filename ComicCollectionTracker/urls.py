from django.conf.urls import url

from ComicCollectionTracker.views import IssueList


urlpatterns = [
    url(r'^$', IssueList.as_view()),
]
