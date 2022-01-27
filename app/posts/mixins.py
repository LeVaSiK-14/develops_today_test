from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from app.posts.serializers import CommentSerializer
from app.posts.models import Comment


class CommentMixin:
    @action(
        methods=[
            "post",
        ],
        detail=True,
        serializer_class=CommentSerializer,
        permission_classes=[
            IsAuthenticated,
        ],
    )
    def add_comment(self, request, *args, **kwargs):
        post = self.get_object()
        user = request.user
        serializer = self.get_serializer_class()(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        comment = Comment.objects.create(
            post=post, author=user, content=data["content"]
        )
        serializer = self.get_serializer_class()(comment).data
        return Response(serializer, status=status.HTTP_201_CREATED)


class UpvoteMixin:
    @action(
        methods=[
            "post",
            'get',
        ],
        detail=True,
    )
    def upvote(self, request, *args, **kwargs):
        post = self.get_object()
        post.add_upvote
        post.save()
        return Response(self.get_serializer_class()(post).data)
