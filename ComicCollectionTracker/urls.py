from django.conf.urls import url

from ComicCollectionTracker.views import \
    IssueListView,\
    ComicvineIssueView,\
    IssueDetailView


urlpatterns = [
    url(r'^$', IssueListView.as_view(), name='collection-index'),
    url(r'^issue/(?P<pk>\d+)$', IssueDetailView.as_view(), name='issue-detail'),
    url(r'^issue/add/', ComicvineIssueView.as_view(), name='add-issue')
    # url(r'^publication/add/', )
]
