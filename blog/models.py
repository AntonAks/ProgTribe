from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel, PageChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtailcodeblock.blocks import CodeBlock

from streams import custom_blocks


class IndexBlogPage(Page):
    """ Home page for blog """
    template = "blog/index_blog_page.html"
    max_count = 1

    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_subtitle = RichTextField(features=["bold", "italic"])
    banner_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    banner_cta = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        ImageChooserPanel("banner_image"),
        PageChooserPanel("banner_cta")
    ]

    class Meta:
        verbose_name = 'Blog Home Page'
        verbose_name_plural = 'Blog Home Pages'


class SimplePage(Page):
    template = "blog/simple_page.html"

    content = StreamField(
        [
            ("title_ant_test", custom_blocks.TitleAndTextBlock())
        ]
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel("content"),
    ]

    class Meta:
        verbose_name = 'Simple Page'
        verbose_name_plural = 'Simple Pages'


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
