from .models import BlogPage
from blog.models import BlogPage
from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register



@register(BlogPage)
class TransHomePageTR(TranslationOptions):
    fields = (
        'text_intro', 'content',
    )
