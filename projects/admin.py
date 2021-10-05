from django.contrib import admin
from projects.models import Issues, Project, Contributor, Commentaire

# Register your models here.
admin.site.register(Issues)
admin.site.register(Project)
admin.site.register(Contributor)
admin.site.register(Commentaire)