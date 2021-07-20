from django.db import models

from blog.models import PostPage


class PostCategory(models.Model):
    title = models.CharField(max_length=1000, verbose_name='Название', blank=True)
    post = models.ForeignKey(PostPage, on_delete=models.CASCADE, verbose_name='Новость',
                             related_name='category', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
