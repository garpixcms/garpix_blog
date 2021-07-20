from django.conf import settings
from django.utils.module_loading import import_string
from django.db import models

BlogMixin = import_string(settings.GARPIX_BLOG_MIXIN)


class BlogPage(BlogMixin, models.Model):
    class Meta:
        verbose_name = "Список Новостей/Акций"
        verbose_name_plural = "Списки Новостей/Акций"
        ordering = ('-created_at',)
