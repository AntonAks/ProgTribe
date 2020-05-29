from django.shortcuts import render
from .models import BlogPage

def archive_page_view(request, month_year_key):

    live_pages = BlogPage.objects.live()
    archive_filtered_list = []
    for page in live_pages:
        if page.first_published_at.strftime("%b %Y") == month_year_key:
            archive_filtered_list.append(page)


    archive_posts = []
    for _page in live_pages:
        archive_posts.append(_page.first_published_at.strftime("%b %Y"))
    archive_posts = set(archive_posts)
    archive_posts = list(archive_posts)

    archive_filtered_list.sort(key=lambda x: x.first_published_at, reverse=True)

    page_content = {
        'live_pages':archive_filtered_list,
        'archive_posts': archive_posts,
        'month_year_key': month_year_key}

    return render(request, 'blog/archive_page.html', context=page_content)
