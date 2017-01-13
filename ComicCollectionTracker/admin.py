from django.contrib import admin

from .models import Collection, Issue, DefaultCollection

admin.site.register(Collection)
admin.site.register(Issue)
admin.site.register(DefaultCollection)
