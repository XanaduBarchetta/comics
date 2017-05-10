from django.conf.urls import url

from ComicCollectionTracker.views import \
    IssueListView,\
    ComicvineIssueView,\
    IssueDetailView, \
    IssueDeleteView


urlpatterns = [
    url(r'^$', IssueListView.as_view(), name='collection-index'),
    url(r'^issue/(?P<pk>\d+)$', IssueDetailView.as_view(), name='issue-detail'),
    url(r'^issue/add/', ComicvineIssueView.as_view(), name='add-issue'),
    url(r'^issue/delete/(?P<pk>\d+)$', IssueDeleteView.as_view(), name='delete-issue'),
    # url(r'^publication/add/', )
]
