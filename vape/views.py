from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from vape.models import Post
from vape.serializers import PostSerializers
from rest_framework.authentication import SessionAuthentication


class PostListAPIView(CreateModelMixin, ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    # authentication_classes = []
    serializer_class = PostSerializers

    def get_queryset(self):
        r = self.request
        print(r.user)
        gs = Post.objects.all()
        return gs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PostCreateAPIView(CreateAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Post.objects.all()
    serializer_class = PostSerializers


class PostDetailAPIView(RetrieveAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Post.objects.all()
    serializer_class = PostSerializers


class PostUpdateAPIView(UpdateAPIView):
        permission_classes = []
        authentication_classes = []
        queryset = Post.objects.all()
        serializer_class = PostSerializers


class PostDeleteAPIView(DestroyAPIView):
        permission_classes = []
        authentication_classes = []
        queryset = Post.objects.all()
        serializer_class = PostSerializers


