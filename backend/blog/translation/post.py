from modeltranslation.translator import TranslationOptions, register
from blog.models import PostPage


@register(PostPage)
class PostPageTranslationOptions(TranslationOptions):
    fields = ('short_description', )
