from .models import BlogPage
from blog.models import BlogPage, BlogListingPage
from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register


@register(BlogPage)
class TransHomePageTR(TranslationOptions):
    fields = (
        'text_intro', 'content',
    )


@register(BlogListingPage)
class TransHomePageTR(TranslationOptions):
    fields = (
        'banner_title',
        'banner_subtitle'
    )
