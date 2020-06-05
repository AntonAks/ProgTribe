from .models import HomePage
from blog.models import BlogPage
from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register


@register(HomePage)
class TransHomePageTR(TranslationOptions):
    fields = (
        'banner_about',
    )


@register(BlogPage)
class TransHomePageTR(TranslationOptions):
    fields = (
        'text_intro', 'content',
    )
