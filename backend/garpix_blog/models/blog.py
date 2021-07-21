from django.conf import settings
from django.utils.module_loading import import_string
from garpix_page.models import BasePage

from app.mixins import PolymorphicActiveMixin

BlogMixin = import_string(settings.GARPIX_BLOG_MIXIN)


class BlogPage(BasePage, BlogMixin, PolymorphicActiveMixin):

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ('-created_at',)
