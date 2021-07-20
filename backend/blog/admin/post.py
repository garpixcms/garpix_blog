from .post_category import PostCategoryItemInline
from .post_image import PostImagesItemInline
from .post_video import PostVideosItemInline
from blog.models import PostPage
from django.contrib import admin
from garpix_page.admin import BasePageAdmin


@admin.register(PostPage)
class PostPageAdmin(BasePageAdmin):
    inlines = [
        PostCategoryItemInline,
        PostImagesItemInline,
        PostVideosItemInline
    ]
    readonly_fields = ('created_at', 'updated_at',)
