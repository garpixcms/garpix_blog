from django.db import models

from blog.models import PostPage
from blog.utils import get_file_path


class PostVideos(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    video = models.FileField(verbose_name="Видео", blank=True, null=True, upload_to=get_file_path)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    post = models.ForeignKey(PostPage, on_delete=models.SET_NULL, related_name='videos', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title', ]
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
