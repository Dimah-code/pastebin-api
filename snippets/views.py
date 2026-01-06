from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly


class SnippetList(generics.ListCreateAPIView):
    """
    List all code snippets and create a new snippet
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update, or delete a code snippet
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (
        IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    )


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
