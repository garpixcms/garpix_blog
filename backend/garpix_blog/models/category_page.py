from django.conf import settings
from django.db import models
from django.utils.module_loading import import_string
from garpix_page.models import BasePage

from app.mixins import PolymorphicActiveMixin
from garpix_blog.models import BlogPage

PostCategoryMixin = import_string(settings.GARPIX_BLOG_POST_CATEGORY_MIXIN)


class CategoryPage(BasePage, PostCategoryMixin, PolymorphicActiveMixin):
    blog = models.ForeignKey(BlogPage, on_delete=models.CASCADE, verbose_name='Блог',
                             related_name='categories', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
