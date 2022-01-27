from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Author(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")
    creation_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
