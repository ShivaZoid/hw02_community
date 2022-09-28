from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    """Модель для сообществ.

    Attributes:
        title: название группы.
        slug: уникальный адрес группы, часть URL
        description: описание сообщества.
    """

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title


class Post(models.Model):
    """Модель для хранения постов.

    Attributes:
        text: текст поста.
        pub_date: дата публикации поста.
        author: автор поста.
        group: возможность, при добавлении новой записи можно было сослаться
               на сообщество.
    """

    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        Group,
        related_name='posts',
        blank=True, null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        # выводим текст поста
        return self.text
