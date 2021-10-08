from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

# Create your views here.
from projects.models import Comment, Project, Issue, Contributor
from projects.permissions import ProjectPermission
from projects.serializers import CommentSerializer, ProjectSerializer, IssueSerializer, ContributorSerializer


class CommentViewset(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        return Comment.objects.all()


class ProjectViewset(ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, ProjectPermission]

    def get_queryset(self):
        return Project.objects.filter(contributor__role="author", contributors=self.request.user)

    def perform_create(self, serializer):
        new_project = serializer.save()
        Contributor.objects.create(
            user=self.request.user,
            project=new_project,
            role="author",
            permission="all"
        )
        new_project.contributors.add(self.request.user)
        new_project.save()

class IssueViewset(ModelViewSet):
    serializer_class = IssueSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Issue.objects.filter()


class ContributorViewset(ModelViewSet):
    serializer_class = ContributorSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Contributor.objects.all()
