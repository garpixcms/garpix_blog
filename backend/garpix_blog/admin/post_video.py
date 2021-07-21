from django.contrib import admin
from garpix_blog.models import PostVideo


@admin.register(PostVideo)
class PostVideoAdmin(admin.ModelAdmin):
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


class PostVideoItemInline(admin.TabularInline):
    model = PostVideo
    fk_name = 'post'
    extra = 1
    show_change_link = True
    fields = ('title', 'video', 'created_at', 'updated_at', 'post')
    readonly_fields = ('created_at', 'updated_at',)
