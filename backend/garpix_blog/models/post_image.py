from django.conf import settings
from django.db import models
from django.utils.module_loading import import_string

from garpix_blog.models import PostPage
from garpix_blog.utils import get_file_path

PostImagesMixin = import_string(settings.GARPIX_BLOG_POST_IMAGE_MIXIN)


class PostImages(PostImagesMixin, models.Model):
    image = models.ImageField(verbose_name="Изображение", blank=True, null=True, upload_to=get_file_path)
    post = models.ForeignKey(PostPage, on_delete=models.SET_NULL, related_name='images', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title', ]
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'
