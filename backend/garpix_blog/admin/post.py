from .post_image import PostImagesItemInline
from .post_video import PostVideoItemInline
from garpix_blog.models import PostPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(PostPage)
class PostPageAdmin(BasePageAdmin):
    inlines = [
        PostImagesItemInline,
        PostVideoItemInline
    ]
    readonly_fields = ('created_at', 'updated_at',)
