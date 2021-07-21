from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db import models
from django.utils.module_loading import import_string
from garpix_page.models import BasePage

from app.mixins import PolymorphicActiveMixin
from garpix_utils.file import get_file_path

PostMixin = import_string(settings.GARPIX_BLOG_POST_MIXIN)


class PostPage(BasePage, PostMixin, PolymorphicActiveMixin):
    short_description = models.TextField(default='', verbose_name='Краткое описание', blank=True)
    short_content = RichTextUploadingField(blank=True, default='', verbose_name='Контент поста')
    image = models.ImageField(verbose_name="Изображение", blank=True, null=True, upload_to=get_file_path)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ('-created_at',)
