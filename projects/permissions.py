from rest_framework import permissions

from projects.models import Project, Comment, Issue


class ProjectPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in ["PUT", "DELETE", "PATCH"]:
            return request.user == obj.author
        return True

class IssuePermission(permissions.BasePermission):

    def has_permission(self, request, view):
        project = Project.objects.get(pk=view.kwargs['id'])
        if request.method in ["POST", "GET"]:
            return request.user in project.contributors.all()
        elif request.method in ["PUT", "DELETE", "PATCH"]:
            return request.user == project.author


class CommentPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        project = Project.objects.get(pk=view.kwargs['id'])
        issue = Issue.objects.get(pk=view.kwargs['issue_id'])
        if request.method in ["POST", "GET"]:
            return request.user in project.contributors.all()
        elif request.method in ["PUT", "DELETE", "PATCH"]:
            return request.user == project.author or request.user == issue.author

class ContributorPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        if request.method in ["POST", "PUT", "DELETE", "PATCH"]:
            project = Project.objects.get(pk=view.kwargs['id'])
            return request.user == project.author
