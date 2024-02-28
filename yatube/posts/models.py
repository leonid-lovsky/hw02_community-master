from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='title',
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='slug',
    )
    description = models.TextField(
        blank=True,
        verbose_name='description',
    )

    def __str__(self) -> str:
        return f'{self.title}'


class Post(models.Model):
    text = models.TextField(
        verbose_name='text',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='pub date',
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='author',
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        related_name='posts',
        blank=True, null=True,
        verbose_name='group',
    )

    def __str__(self) -> str:
        return f'{self.__class__.__name__} {self.pk}'

    class Meta:
        ordering = ('-pub_date',)
