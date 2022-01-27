from rest_framework.routers import SimpleRouter

from app.accounts.views import RegistrationAPIView

router = SimpleRouter()

router.register('users', RegistrationAPIView)

urlpatterns = []

urlpatterns += router.urls
