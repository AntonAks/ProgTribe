from django.db import models
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks
from blog.models import BlogPage
from django.utils.datastructures import MultiValueDictKeyError
from django.core.mail import send_mail

from random import choice

try:
    from local_site_settings import local_site_settings
    from local_site_settings import *
except ImportError:
    from _local_site_settings import local_site_settings
    from _local_site_settings import *


class HomePage(Page):
    """ Home page for blog """

    template = "home/home_page.html"
    max_count = 1

    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_subtitle = RichTextField(features=["bold", "italic"], default='')
    banner_about = RichTextField(features=["bold", "italic"], default='')
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
        FieldPanel("banner_about"),
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

        all_child_pages = self.get_children().live().specific().filter(blogpage__page_category='Common Page').order_by('-first_published_at')

        paginator = Paginator(all_child_pages, 6)

        page = request.GET.get("page")

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        archive_posts = []
        for _page in all_child_pages:
            if _page.first_published_at:
                archive_posts.append(_page.first_published_at.strftime("%b %Y"))

        archive_posts = set(archive_posts)
        archive_posts = list(archive_posts)

        context["sub_pages"] = posts
        context["archive_posts"] = archive_posts
        context["local_site_settings"] = local_site_settings

        if all_child_pages:
            context["random_post"] = choice(all_child_pages)

        return context


class AboutPage(Page):
    """ Home page for blog """

    template = "home/about_page.html"
    max_count = 1

    content = StreamField(
        [
            ('content', blocks.RichTextBlock())
        ],
        blank=True,
        null=True,
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('content'),
    ]

    class Meta:
        verbose_name = 'About Page'
        verbose_name_plural = 'About Pages'

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        live_pages = BlogPage.objects.live().filter(page_category='Common Page')

        archive_posts = []
        for _page in live_pages:
            if _page.first_published_at:
                archive_posts.append(_page.first_published_at.strftime("%b %Y"))

        archive_posts = set(archive_posts)
        archive_posts = list(archive_posts)

        context["archive_posts"] = archive_posts
        context["local_site_settings"] = local_site_settings

        if live_pages:
            context["random_post"] = choice(live_pages)

        if request.method == 'POST':
            try:
                feedback_name = request.POST['mainFeedbackForm_Name']
                feedback_email = request.POST['mainFeedbackForm_EMail']
                feedback_text = request.POST['mainFeedbackForm_Text']

                send_mail(subject="New Feedback",
                          message=f"From:{feedback_name} \n"
                                  f"Mail:{feedback_email} \n"
                                  f"{feedback_text}",
                          from_email=EMAIL_HOST_USER,
                          recipient_list=[EMAIL_HOST_USER],
                          fail_silently=False
                          )

            except MultiValueDictKeyError:
                search_text = ''

        return context
