from django.db import models
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
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
    template = "blog/home.html"
    max_count = 1

    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_subtitle = RichTextField(features=["bold", "italic"], default='')
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

    def get_child_pages(self):
        pages = Page.get_children(self)
        return pages

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        all_child_pages = self.get_children().specific().order_by('-first_published_at')

        paginator = Paginator(all_child_pages, 3)

        page = request.GET.get("page")

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        context["sub_pages"] = posts
        context["last_post"] = all_child_pages[0]
        context["last_post_2"] = all_child_pages[1]
        return context


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
