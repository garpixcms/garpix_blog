from modeltranslation.translator import TranslationOptions, register
from garpix_blog.models import PostPage


@register(PostPage)
class PostPageTranslationOptions(TranslationOptions):
    fields = ('short_description', )
