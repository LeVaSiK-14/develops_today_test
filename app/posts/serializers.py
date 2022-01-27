from rest_framework import serializers

from app.posts.models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    post = serializers.ReadOnlyField(source='post.title')
    class Meta:
        model = Comment
        fields = [
            "id",
            "content",
            "post",
            "author",
            "creation_date",
        ]
        read_only_fields = [
            "post",
            "author",
            "creation_date",
        ]


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "author",
            "link",
            "amount_of_upvotes",
            "creation_date",
            "comments",
        ]
        read_only_fields = [
            "author",
            "amount_of_upvotes",
            "creation_date",
            "comments",
        ]
