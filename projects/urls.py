from rest_framework.routers import DefaultRouter
from projects.views import CommentViewset, ContributorViewset, ProjectViewset, IssueViewset


router = DefaultRouter()
router.register(r'', ProjectViewset, basename="projects")
router.register(r"^(?P<id>[^/.]+)/contributors", ContributorViewset, basename="contributors")
router.register(r"^(?P<id>[^/.]+)/issues", IssueViewset, basename="issues")
router.register(r"^(?P<id>[^/.]+)/issues/(?P<issue_id>[^/.]+)/comments", CommentViewset, basename="comment")

urlpatterns = router.urls