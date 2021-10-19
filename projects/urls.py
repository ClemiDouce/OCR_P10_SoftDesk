from rest_framework.routers import DefaultRouter
from projects.views import CommentViewset, ContributorViewset, ProjectViewset, IssueViewset


router = DefaultRouter()
router.register(r"projects", ProjectViewset, basename="projects")
router.register(r"projects/(?P<id>[^/.]+)/users", ContributorViewset, basename="users")
router.register(r"projects/(?P<id>[^/.]+)/issues", IssueViewset, basename="issues")
router.register(r"projects/(?P<id>[^/.]+)/issues/(?P<issue_id>[^/.]+)/comments", CommentViewset, basename="comment")


urlpatterns = router.urls