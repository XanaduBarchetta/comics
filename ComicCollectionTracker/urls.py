from django.conf.urls import url

from ComicCollectionTracker.views import IssueListView, ComicvineIssueView


urlpatterns = [
    url(r'^$', IssueListView.as_view(), name='collection-index'),
    url(r'^issue/add/', ComicvineIssueView.as_view())
    # url(r'^publication/add/', )
]
