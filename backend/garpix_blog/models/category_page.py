from django.conf import settings
from django.utils.module_loading import import_string
from garpix_page.models import BasePage
from garpix_utils.models import PolymorphicActiveMixin

from garpix_blog.paginators import BlogPagination

PostCategoryMixin = import_string(settings.GARPIX_BLOG_POST_CATEGORY_MIXIN)


class CategoryPage(BasePage, PostCategoryMixin, PolymorphicActiveMixin):

    def get_context(self, request=None, *args, **kwargs):
        from garpix_blog.models import PostPage
        context = super().get_context(request, *args, **kwargs)

        paginator = BlogPagination()
        posts = PostPage.on_site.filter(is_active=True, parent=kwargs['object'], category=self)
        page_posts = paginator.paginate_queryset(posts, request)

        context.update({
            'posts': paginator.get_paginated_response(page_posts),
        })
        return context

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ('-created_at',)
