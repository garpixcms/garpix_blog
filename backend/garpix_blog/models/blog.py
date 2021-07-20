from django.conf import settings
from django.utils.module_loading import import_string

BlogMixin = import_string(settings.GARPIX_BLOG_MIXIN)


class BlogPage(BlogMixin):
    class Meta:
        verbose_name = "Список Новостей/Акций"
        verbose_name_plural = "Списки Новостей/Акций"
        ordering = ('-created_at',)
