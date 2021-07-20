from django.contrib import admin
from blog.models import PostVideos


@admin.register(PostVideos)
class PostVideosAdmin(admin.ModelAdmin):
    list_display = ('title', 'post')
    fieldsets = [
        [
            None, {
                'fields': (
                    'title', 'video', 'created_at', 'updated_at', 'post'
                )
            }
        ],
    ]
    ordering = ('-created_at',)
    search_fields = ('status',)
    readonly_fields = ('created_at', 'updated_at',)


class PostVideosItemInline(admin.TabularInline):
    model = PostVideos
    extra = 1
    show_change_link = True
    fields = ('title', 'video', 'created_at', 'updated_at', 'post')
    readonly_fields = ('created_at', 'updated_at',)
