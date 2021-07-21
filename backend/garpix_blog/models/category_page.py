from django.conf import settings
from django.utils.module_loading import import_string
from garpix_page.models import BasePage

from app.mixins import PolymorphicActiveMixin

PostCategoryMixin = import_string(settings.GARPIX_BLOG_POST_CATEGORY_MIXIN)


class CategoryPage(BasePage, PostCategoryMixin, PolymorphicActiveMixin):
    template = 'pages/category.html'

    def get_context(self, request=None, *args, **kwargs):
        from garpix_blog.models import PostPage
        context = super().get_context(request, *args, **kwargs)
        posts = PostPage.on_site.filter(is_active=True, parent=kwargs['object'])[:10]
        context.update({
            'posts': posts
        })
        return context

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ('-created_at',)
