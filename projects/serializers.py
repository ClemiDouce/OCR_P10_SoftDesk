from rest_framework.serializers import ModelSerializer

from projects.models import Project, Contributor, Comment, Issue


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class ContributorSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = "__all__"
        read_only_fields = ('user', 'project')


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = "__all__"
