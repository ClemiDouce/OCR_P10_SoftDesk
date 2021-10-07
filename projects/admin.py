from django.contrib import admin
from projects.models import Issue, Project, Contributor, Comment

# Register your models here.
admin.site.register(Issue)
admin.site.register(Project)
admin.site.register(Contributor)
admin.site.register(Comment)