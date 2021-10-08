from rest_framework import permissions

class ProjectPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in ["POST", "GET"]:
            return True
        elif request.method in ["PUT", "DELETE", "PATCH"]:
            return request.user in obj.contributors.get(contributor__role="author")

class IssuePermission(permissions.BasePermission):

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in ["POST", "GET"]:
            return request.user in obj.contributors.all()
        elif request.method in ["PUT", "DELETE", "PATCH"]:
            return request.user in obj.contributors.all()