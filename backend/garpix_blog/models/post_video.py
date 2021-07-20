from django.conf import settings
from django.db import models
from django.utils.module_loading import import_string

from garpix_blog.models import PostPage
from garpix_blog.utils import get_file_path

PostVideosMixin = import_string(settings.GARPIX_BLOG_POST_VIDEO_MIXIN)


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
