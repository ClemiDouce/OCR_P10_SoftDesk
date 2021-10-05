from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from auth.views import RegisterView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name="login"),
    path('login/refresh/', TokenRefreshView.as_view(), name="token-refresh"),
    path('register/', RegisterView.as_view(), name="register")
]