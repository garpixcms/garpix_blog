from django.contrib import admin
from garpix_blog.models import CategoryPage


@admin.register(CategoryPage)
class CategoryPageAdmin(admin.ModelAdmin):
    list_display = ('title',)
    fieldsets = [
        [
            None, {
                'fields': (
                    'title',
                )
            }
        ],
    ]
