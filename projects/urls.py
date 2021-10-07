from rest_framework.routers import DefaultRouter
from projects.views import CommentViewset, ContributorViewset, ProjectViewset, IssueViewset


router = DefaultRouter()
router.register('projects', ProjectViewset, basename="projects")
router.register('comments', CommentViewset, basename="comment")
router.register('issues', IssueViewset, basename="issues")
router.register('contributors', ContributorViewset, basename="contributors")

urlpatterns = router.urls