from modeltranslation.translator import TranslationOptions, register
from garpix_blog.models import BlogPage


@register(BlogPage)
class BlogPageTranslationOptions(TranslationOptions):
    pass
