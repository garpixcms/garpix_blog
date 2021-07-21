from django.contrib import admin
from garpix_blog.models import CategoryPage


@admin.register(CategoryPage)
class CategoryPageAdmin(admin.ModelAdmin):
    list_display = ('title', 'blog')
    fieldsets = [
        [
            None, {
                'fields': (
                    'title', 'blog',
                )
            }
        ],
    ]
    search_fields = ('status',)


class CategoryPageItemInline(admin.TabularInline):
    model = CategoryPage
    fk_name = 'blog'
    extra = 1
    show_change_link = True
    fields = ('title', 'blog')
