from django.conf import settings
from django.utils.module_loading import import_string
from garpix_page.models import BasePage

from app.mixins import PolymorphicActiveMixin

BlogMixin = import_string(settings.GARPIX_BLOG_MIXIN)


class BlogPage(BasePage, BlogMixin, PolymorphicActiveMixin):
    template = 'pages/blog.html'

    def get_context(self, request=None, *args, **kwargs):
        from garpix_blog.models import CategoryPage, PostPage
        context = super().get_context(request, *args, **kwargs)
        categories = CategoryPage.on_site.filter(is_active=True, parent=kwargs['object'])[:10]
        posts = PostPage.on_site.filter(is_active=True, parent=kwargs['object'])[:10]
        context.update({
            'categories': categories,
            'posts': posts
        })
        return context

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ('-created_at',)
