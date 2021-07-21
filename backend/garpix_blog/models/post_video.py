from django.conf import settings
from django.db import models
from django.utils.module_loading import import_string
from garpix_page.models import BasePage

from app.mixins import PolymorphicActiveMixin
from garpix_blog.models import PostPage
from garpix_utils.file import get_file_path

PostVideosMixin = import_string(settings.GARPIX_BLOG_POST_VIDEO_MIXIN)


class PostVideo(BasePage, PostVideosMixin, PolymorphicActiveMixin):
    video = models.FileField(verbose_name="Видео", upload_to=get_file_path)
    post = models.ForeignKey(PostPage, on_delete=models.CASCADE, related_name='videos', verbose_name='Новость/Акция')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title', ]
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'
