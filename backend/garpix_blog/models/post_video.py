from django.conf import settings
from django.db import models
from django.utils.module_loading import import_string
from garpix_utils.models import ActiveMixin

from garpix_blog.models import PostPage
from garpix_utils.file import get_file_path

PostVideosMixin = import_string(settings.GARPIX_BLOG_POST_VIDEO_MIXIN)


class PostVideo(PostVideosMixin, ActiveMixin):
    title = models.CharField(max_length=255, verbose_name='Название')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    video = models.FileField(verbose_name="Видео", upload_to=get_file_path)
    post = models.ForeignKey(PostPage, on_delete=models.CASCADE, related_name='videos', verbose_name='Пост')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title', ]
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
