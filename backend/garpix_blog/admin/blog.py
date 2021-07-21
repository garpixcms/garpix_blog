from garpix_blog.admin.category_page import CategoryPageItemInline
from garpix_blog.models import BlogPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(BlogPage)
class BlogPageAdmin(BasePageAdmin):
    inlines = [
        CategoryPageItemInline,
    ]
