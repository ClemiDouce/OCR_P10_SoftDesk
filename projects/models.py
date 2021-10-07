from django.conf import settings
from django.db import models


class Project(models.Model):

    PROJECT_TYPES = (
        ('back', 'Back-end'),
        ('front', 'Front-end'),
        ('ios', 'iOS'),
        ('android', 'Android'),
    )

    titre = models.CharField(max_length=30)
    description = models.CharField(max_length=1000, blank=True, null=True)
    type = models.TextField(choices=PROJECT_TYPES, default="back")
    contributors = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Contributor')

    def __str__(self):
        return self.titre


class Contributor(models.Model):

    ROLES = (
        ('author', 'Author'),
        ('responsable', 'Responsable'),
        ('contributor', 'Contributor')
    )

    PERMISSIONS = (
        ('restricted', 'Contributor'),
        ('all', 'Author')
    )

    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    role = models.CharField(choices=ROLES, max_length=20, default="contributor")
    permission = models.CharField(choices=PERMISSIONS, max_length=20, default="restricted")

    def __str__(self):
        return f"{self.user.username},{self.role}"

    class Meta:
        unique_together = [['user', 'project']]


class Issue(models.Model):

    PRIORITY = (
        ('low', 'Low'),
        ('mid', 'Middle'),
        ('high', 'High')
    )

    BALISE = (
        ('bug', 'Bug'),
        ('amelioration', 'Amelioration'),
        ('tache', 'Tache'),
    )

    STATUS = (
        ('todo', 'To Do'),
        ('inprogress', 'In Progress'),
        ('done', 'Done')
    )

    title = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    tag = models.CharField(choices=BALISE, max_length=12, default="bug")
    priority = models.CharField(choices=PRIORITY, max_length=12, default="low")
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, max_length=20, default="todo")
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='author')
    assigne = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='assigne')
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

class Comment(models.Model):
    description = models.TextField(max_length=200)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    issues = models.ForeignKey(to=Issue, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description[:10]
