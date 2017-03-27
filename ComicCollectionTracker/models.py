from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Issue(models.Model):
    # metadata
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comicvine_id = models.CharField(max_length=100)
    # issue data
    publication = models.CharField(max_length=300)  # The title of the series, e.g., Superman, Detective Comics, etc.
    number = models.IntegerField
    printing = models.CharField(max_length=100, default="1")
    cover = models.CharField('Cover number or letter', max_length=100)
    cover_url = models.CharField(max_length=500)
    on_sale_date = models.DateField
    issue_comment = models.TextField(default=None)
    # collection data
    own_physical = models.BooleanField(default=False)
    own_digital = models.BooleanField(default=False)
    have_read = models.BooleanField(default=False)
    collection_comment = models.TextField(default=None)

    def __str__(self):
        return "%s #%s" % (self.publication, self.number)

    # TODO: add sort method
