from rest_framework import generics
from rest_framework.permissions import AllowAny

from auth.serializers import RegisterSerializer
from django.contrib.auth.models import User

# Create your views here.

class RegisterView(generics.CreateAPIView):
    authentication_classes = []

    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
