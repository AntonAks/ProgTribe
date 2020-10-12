from django.db import models
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks
from blog.models import BlogPage, BlogPageTag
from tools.models import Feedback
from django.core.exceptions import ObjectDoesNotExist

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from random import choice


try:
    from local_site_settings import local_site_settings
    from local_site_settings import *
except ImportError:
    from _local_site_settings import local_site_settings
    from _local_site_settings import *


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


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

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        all_child_pages = self.get_children().live().specific().filter(blogpage__page_category='Common Page').order_by('-first_published_at')

        if request.GET.get('tag', None):
            tags = request.GET.get('tag')
            all_child_pages = all_child_pages.filter(blogpage__tags__slug__in=[tags])

        paginator = Paginator(all_child_pages, 6)

        page = request.GET.get("page")

        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        all_tags = list(set([i.tag for i in BlogPageTag.objects.all()]))

        context["sub_pages"] = posts
        context["all_tags"] = all_tags
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

    def get_path_page(self):
        if self.url_path == '/home/':
            return "/"
        return self.slug

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        client_ip = get_client_ip(request)
        context["feedback_button_activation"] = False

        try:
            client_feedback_from_db = Feedback.objects.get(feedback_client_id__exact=client_ip)
            context["feedback_time_left"] = client_feedback_from_db.get_time_left_for_feedback()
            if client_feedback_from_db.is_older_then_hour():
                context["feedback_button_activation"] = True
        except ObjectDoesNotExist:
            context["feedback_button_activation"] = True

        live_pages = BlogPage.objects.live().filter(page_category='Common Page')
        all_tags = [i.tag for i in BlogPageTag.objects.all()]

        context["all_tags"] = all_tags
        context["local_site_settings"] = local_site_settings

        if live_pages:
            context["random_post"] = choice(live_pages)

        if request.method == 'POST':

            feedback_name = request.POST['mainFeedbackForm_Name']
            feedback_email = request.POST['mainFeedbackForm_EMail']
            feedback_text = request.POST['mainFeedbackForm_Text']

            try:
                client_feedback_from_db = Feedback.objects.get(feedback_client_id__exact=client_ip)
                client_feedback_from_db.feedback_name = feedback_name
                client_feedback_from_db.feedback_email = feedback_email
                client_feedback_from_db.save()
                context["feedback_time_left"] = client_feedback_from_db.get_time_left_for_feedback()

            except ObjectDoesNotExist:
                new_feedback = Feedback()
                new_feedback.feedback_client_id = client_ip
                new_feedback.feedback_name = feedback_name
                new_feedback.feedback_email = feedback_email
                new_feedback.save()

                context["feedback_time_left"] = new_feedback.get_time_left_for_feedback()

            message = Mail(
                from_email='progtribe@gmail.com',
                to_emails='progtribe@gmail.com',
                subject="New Feedback",
                html_content=f"<p>From: {feedback_name} </p>"
                             f"<p>Mail: {feedback_email} </p>"
                             f"<p>{feedback_text}</p>")

            if context["feedback_button_activation"]:
                sg = SendGridAPIClient(SENDGRID_API_KEY)
                sg.send(message)

            context["feedback_button_activation"] = False

        return context
