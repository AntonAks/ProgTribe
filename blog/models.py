from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtailcodeblock.blocks import CodeBlock

class BlogIndexPage(Page):
    pass


class BlogPage(Page):
    description = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )

    image = models.ImageField(blank=True, null=True)

    content = StreamField(
        [
            ('heading', blocks.CharBlock()),
            ('content', blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
            ('codeblock', CodeBlock(label='Code'))
        ],
        blank=True,
        null=True,

    )

    content_panels = Page.content_panels + [
        FieldPanel('description'), 
        FieldPanel('image'),
        StreamFieldPanel('content'),
    ]