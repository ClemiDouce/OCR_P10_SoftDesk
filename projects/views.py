from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

# Create your views here.
from projects.models import Comment, Project, Issue, Contributor
from projects.permissions import ProjectPermission, ContributorPermission, CommentPermission, \
    IssuePermission
from projects.serializers import CommentSerializer, ProjectSerializer, IssueSerializer, ContributorSerializer


class CommentViewset(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [CommentPermission]


    def get_queryset(self):
        return Comment.objects.all()

    def perform_create(self, serializer):
        issue = get_object_or_404(Issue, pk=self.kwargs['issue_id'])
        serializer.save(author=self.request.user, issues=issue)


class ProjectViewset(ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [ProjectPermission]

    def get_queryset(self):
        return Project.objects.filter(contributors=self.request.user)

    def perform_create(self, serializer):
        new_project = serializer.save(author=self.request.user)
        Contributor.objects.create(
            user=self.request.user,
            project=new_project,
            permission="all"
        )
        new_project.contributors.add(self.request.user)
        new_project.save()

class IssueViewset(ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [IssuePermission]

    def get_queryset(self):
        project = get_object_or_404(Project, pk=self.kwargs['id'])
        return Issue.objects.filter(project=project)

    def perform_create(self, serializer):
        project = get_object_or_404(Project, pk=self.kwargs['id'])
        serializer.save(project=project, author=self.request.user, assigne=self.request.user)


class ContributorViewset(ModelViewSet):
    serializer_class = ContributorSerializer
    permission_classes = [ContributorPermission]

    def get_queryset(self):
        print(self.request.user)
        project = get_object_or_404(Project, pk=self.kwargs['id'])
        return Contributor.objects.filter(project=project)

    # def perform_create(self, serializer):
    #     project = get_object_or_404(Project, pk=self.kwargs['id'])
    #     user = get_object_or_404(User, email=self.request.POST['email'])
    #     serializer.save(user=user, project=project)

    def create(self, request, *args, **kwargs):
        project = get_object_or_404(Project, pk=self.kwargs['id'])
        user = get_object_or_404(User, email=self.request.POST['email'])
        serializer = self.get_serializer(data={'user':user.pk, 'project':project.pk, 'permission':'restricted'})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)