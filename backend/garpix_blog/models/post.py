from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db import models
from django.utils.module_loading import import_string
from garpix_page.models import BasePage
from garpix_utils.file import get_file_path

from garpix_utils.models import PolymorphicActiveMixin

PostMixin = import_string(settings.GARPIX_BLOG_POST_MIXIN)


class PostPage(BasePage, PostMixin, PolymorphicActiveMixin):
    short_content = models.TextField(default='', verbose_name='Краткое описание', blank=True)
    content = RichTextUploadingField(default='', verbose_name='Контент поста')
    image = models.ImageField(verbose_name="Изображение", blank=True, null=True, upload_to=get_file_path)
    category = models.ForeignKey('CategoryPage', null=True, on_delete=models.CASCADE, verbose_name='Категория',
                                 related_name='category_posts')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ('-created_at',)
