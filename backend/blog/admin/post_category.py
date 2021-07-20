from django.contrib import admin
from blog.models import PostCategory


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'post')
    fieldsets = [
        [
            None, {
                'fields': (
                    'title', 'post',
                )
            }
        ],
    ]
    search_fields = ('status',)


class PostCategoryItemInline(admin.TabularInline):
    model = PostCategory
    extra = 1
    show_change_link = True
    fields = ('title', 'post')
