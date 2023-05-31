from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (IsAuthenticatedOrReadOnly,
                                        IsAuthenticated)

from .permissions import AuthorOrReadOnly, ReadOnly
from .serializers import (PostSerializer, GroupSerializer,
                          FollowSerializer, CommentSerializer)
from posts.models import Post, Group, User


class BasePermissionViewSet(viewsets.ModelViewSet):
    permission_classes = (AuthorOrReadOnly,)

    def get_permissions(self):
        if self.action in ('retrieve', 'get'):
            return ReadOnly(),
        if self.action == 'post':
            return IsAuthenticatedOrReadOnly(),
        return super().get_permissions()


class PostViewSet(BasePermissionViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        user = get_object_or_404(User, pk=self.request.user.pk)
        return user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentViewSet(BasePermissionViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return self.get_post().comments

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())

    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))
