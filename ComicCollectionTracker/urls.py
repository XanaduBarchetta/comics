from django.conf.urls import url

from . import views
from ComicCollectionTracker.views import IssueList


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^collection/', IssueList)
]
