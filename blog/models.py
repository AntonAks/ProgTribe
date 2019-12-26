from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtailcodeblock.blocks import CodeBlock


class IndexBlogPage(Page):
    pass


class BlogPage(Page):

    title_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content = StreamField(
        [
            ('heading', blocks.CharBlock()),
            ('advice_hint', blocks.RichTextBlock()),
            ('warning_hint', blocks.RichTextBlock()),
            ('content', blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
            ('codeblock', CodeBlock(label='Code'))
        ],
        blank=True,
        null=True,
    )

    content_panels = Page.content_panels + [
        ImageChooserPanel('title_image'),
        StreamFieldPanel('content'),
    ]
