from django.contrib import admin
from garpix_blog.models import PostImage


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'post')
    fieldsets = [
        [
            None, {
                'fields': (
                    'title', 'image', 'created_at', 'updated_at', 'post'
                )
            }
        ],
    ]
    ordering = ('-created_at',)
    search_fields = ('status',)
    readonly_fields = ('created_at', 'updated_at',)


class PostImageItemInline(admin.TabularInline):
    model = PostImage
    fk_name = 'post'
    extra = 1
    show_change_link = True
    fields = ('title', 'image', 'created_at', 'updated_at', 'post')
    readonly_fields = ('created_at', 'updated_at',)
