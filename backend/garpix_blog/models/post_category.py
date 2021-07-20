from django.conf import settings
from django.db import models
from django.utils.module_loading import import_string

from garpix_blog.models import PostPage

PostCategoryMixin = import_string(settings.GARPIX_BLOG_POST_CATEGORY_MIXIN)


class PostCategory(PostCategoryMixin, models.Model):
    post = models.ForeignKey(PostPage, on_delete=models.CASCADE, verbose_name='Новость',
                             related_name='categories', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
