from celery import shared_task
from app.posts.models import Post


@shared_task
def annul_upvote():
    for post in Post.objects.all():
        post.amount_of_upvotes = 0
        post.save()