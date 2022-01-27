from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from app.posts.serializers import PostSerializer
from app.posts.models import Post
from app.posts.mixins import CommentMixin, UpvoteMixin


class PostModelViewSet(ModelViewSet, CommentMixin, UpvoteMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]

    def perform_create(self, serializer):
        
        return serializer.save(author=self.request.user)
