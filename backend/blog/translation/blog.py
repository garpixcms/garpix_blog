from modeltranslation.translator import TranslationOptions, register
from blog.models import BlogPage


@register(BlogPage)
class BlogPageTranslationOptions(TranslationOptions):
    pass
