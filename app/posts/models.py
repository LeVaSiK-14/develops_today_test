from django.db import models

from app.posts.utils import Author


class Post(Author):
    title = models.CharField(verbose_name="Заголовок", max_length=127)
    link = models.URLField(verbose_name="Ссылка", max_length=1028)
    amount_of_upvotes = models.PositiveIntegerField(
        verbose_name="Количество голосов", default=0
    )

    @property
    def add_upvote(self):
        self.amount_of_upvotes += 1

    def __str__(self):
        return f"{self.author.username} --- {self.title}"

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"


class Comment(Author):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField(verbose_name="Сообщение")

    def __str__(self):
        return f"{self.author.username} --- {self.content}"

    class Meta:
        verbose_name = "Коммент"
        verbose_name_plural = "Комменты"
