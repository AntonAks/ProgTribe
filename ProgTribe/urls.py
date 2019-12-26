from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path, include

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from .views import HomePageView, IndexPageView, BlogPageView

urlpatterns = [
                  path('', HomePageView.as_view(), name='home'),
                  path('admin/', admin.site.urls),
                  # path('blog/', BlogPageView.as_view(), name='blog'),
                  path('index/', IndexPageView.as_view(), name='index'),

                  re_path(r'^cms/', include(wagtailadmin_urls), name='cms'),
                  re_path(r'^documents/', include(wagtaildocs_urls)),
                  re_path(r'^blog/', include(wagtail_urls)),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
