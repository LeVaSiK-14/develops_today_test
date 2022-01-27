from rest_framework.routers import SimpleRouter

from app.posts.views import PostModelViewSet

router = SimpleRouter()

router.register("post", PostModelViewSet)

urlpatterns = []

urlpatterns += router.urls
