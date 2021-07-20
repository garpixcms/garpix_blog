from django.conf import settings
from django.db import models
from django.utils.module_loading import import_string

from garpix_blog.models import PostPage
from garpix_blog.utils import get_file_path

PostVideosMixin = import_string(settings.GARPIX_BLOG_POST_VIDEO_MIXIN)


class PostVideos(PostVideosMixin, models.Model):
    video = models.FileField(verbose_name="Видео", blank=True, null=True, upload_to=get_file_path)
    post = models.ForeignKey(PostPage, on_delete=models.SET_NULL, related_name='videos', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title', ]
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
