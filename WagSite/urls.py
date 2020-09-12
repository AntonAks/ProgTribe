from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path, re_path

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from search import views as search_views

from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('dj_admin/', admin.site.urls),
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^search/$', search_views.search, name='search'),

]


urlpatterns += i18n_patterns(
    url(r'', include(wagtail_urls)),
)
