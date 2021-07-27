from django.conf import settings
from django.utils.module_loading import import_string
from garpix_page.models import BasePage
from rest_framework.pagination import PageNumberPagination

from garpix_blog.mixins import PolymorphicActiveMixin

BlogMixin = import_string(settings.GARPIX_BLOG_MIXIN)


class BlogPage(BasePage, BlogMixin, PolymorphicActiveMixin):

    def get_context(self, request=None, *args, **kwargs):
        from garpix_blog.models import CategoryPage, PostPage
        context = super().get_context(request, *args, **kwargs)

        paginator = PageNumberPagination()

        categories = CategoryPage.on_site.filter(is_active=True, parent=kwargs['object'])
        posts = PostPage.on_site.filter(is_active=True, parent=kwargs['object'])

        page_posts = paginator.paginate_queryset(posts, request)
        page_categories = paginator.paginate_queryset(categories, request)

        context.update({
            'posts': paginator.get_paginated_response(page_posts),
            'categories': paginator.get_paginated_response(page_categories),
        })
        return context

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ('-created_at',)
