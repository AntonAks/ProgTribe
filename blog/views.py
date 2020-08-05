from django.shortcuts import render
from .models import BlogPage

from random import choice

try:
    from local_site_settings import local_site_settings
except ImportError:
    from _local_site_settings import local_site_settings


def archive_page_view(request, month_year_key):

    live_pages = BlogPage.objects.live()
    archive_filtered_list = []
    for page in live_pages:
        if page.first_published_at.strftime("%b %Y") == month_year_key:
            print(page.first_published_at.strftime("%b %Y"))
            archive_filtered_list.append(page)

    archive_posts = []
    for _page in live_pages:
        if _page.first_published_at:
            archive_posts.append(_page.first_published_at.strftime("%b %Y"))
    archive_posts = set(archive_posts)
    archive_posts = list(archive_posts)

    archive_filtered_list.sort(key=lambda x: x.first_published_at, reverse=True)

    page_content = {'live_pages': archive_filtered_list,
                    "local_site_settings": local_site_settings,
                    'archive_posts': archive_posts,
                    'month_year_key': month_year_key,
                    "random_post": choice(live_pages)}

    return render(request, 'blog/archive_page.html', context=page_content)
