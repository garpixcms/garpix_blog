from django.conf import settings
from django.utils.module_loading import import_string
from garpix_page.models import BasePage

from garpix_utils.models import PolymorphicActiveMixin
from garpix_blog.paginators import BlogPagination

BlogMixin = import_string(settings.GARPIX_BLOG_MIXIN)


class BlogPage(BasePage, BlogMixin, PolymorphicActiveMixin):

    def get_context(self, request=None, *args, **kwargs):
        from garpix_blog.models import CategoryPage, PostPage
        context = super().get_context(request, *args, **kwargs)
        paginator = BlogPagination()

        categories = CategoryPage.on_site.filter(is_active=True, parent=kwargs['object'])
        posts = PostPage.on_site.filter(is_active=True, parent=kwargs['object'])

        page_posts = paginator.paginate_queryset(posts, request)
        context.update({
            'categories': categories,
            'posts': paginator.get_paginated_response(page_posts),
        })
        return context

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ('-created_at',)
