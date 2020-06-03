from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtailcodeblock.blocks import CodeBlock

from random import choice


class BlogPage(Page):
    title_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    text_intro = RichTextField(blank=False, default='Short description', null=True, max_length=300)

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
        FieldPanel('text_intro'),
        StreamFieldPanel('content'),
    ]

    def get_title_image(self):
        return self.title_image

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        all_child_pages = self.get_parent().get_children().specific().order_by('-first_published_at')

        archive_posts = []
        for _page in all_child_pages:
            archive_posts.append(_page.first_published_at.strftime("%b %Y"))
        archive_posts = set(archive_posts)
        archive_posts = list(archive_posts)

        context["archive_posts"] = archive_posts
        # context["random_post"] = choice(all_child_pages)

        return context
