from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel, CharField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtailcodeblock.blocks import CodeBlock
from modelcluster.fields import ParentalKey
from taggit.models import TaggedItemBase
from modelcluster.contrib.taggit import ClusterTaggableManager

from random import choice

try:
    from local_site_settings import local_site_settings
except ImportError:
    from _local_site_settings import local_site_settings


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE,
    )


class BlogPage(Page):
    template = "blog/blog_page.html"

    PAGE_CATEGORIES = [('Common Page', 'Common Page'), ('Common Page', 'Single Page')]

    title_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    text_intro = RichTextField(blank=False, default='Short description', null=True, max_length=600)
    page_category = CharField(max_length=100, choices=PAGE_CATEGORIES, default='Common Page')
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    content = StreamField(
        [
            ('heading', blocks.CharBlock()),
            ('advice_hint', blocks.RichTextBlock()),
            ('warning_hint', blocks.RichTextBlock()),
            ('terminal_block', blocks.RichTextBlock()),
            ('content', blocks.RichTextBlock()),
            ('image', ImageChooserBlock()),
            ('codeblock', CodeBlock(label='Code'))
        ],
        blank=True,
        null=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel('page_category'),
        ImageChooserPanel('title_image'),
        FieldPanel("tags"),
        FieldPanel('text_intro'),
        StreamFieldPanel('content'),
    ]

    def __str__(self):
        return f"title: {self.title}, tags: {self.tags}"

    def get_title_image(self):
        return self.title_image

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        all_child_pages = self.get_parent().get_children().specific().live().filter(blogpage__page_category='Common Page').order_by('-first_published_at')

        archive_posts = []
        for _page in all_child_pages:
            if _page.first_published_at:
                archive_posts.append(_page.first_published_at.strftime("%b %Y"))

        archive_posts = set(archive_posts)
        archive_posts = list(archive_posts)

        context["archive_posts"] = archive_posts
        context["local_site_settings"] = local_site_settings
        if all_child_pages:
            context["random_post"] = choice(all_child_pages)

        return context
