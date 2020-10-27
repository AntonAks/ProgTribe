from django.db import models
from background_task import background
from . import get_dou_news, get_itc_news, get_liga_news


class NewsContent(models.Model):

    web_resource_name = models.CharField(max_length=255, null=False)
    post_name_title = models.CharField(max_length=500, null=False)
    post_ulr = models.CharField(max_length=1000, null=False)
    update_timestamp = models.DateTimeField(null=False, blank=True, auto_now=True)

    class Meta:
        verbose_name_plural = 'News Content'
        ordering = ['web_resource_name', 'post_name_title']

    def __str__(self):
        return f"{self.web_resource_name},  {self.post_name_title.__str__()}"

    @staticmethod
    def store_to_db(source_from, **kwargs):
        titles = kwargs['titles']
        urls = kwargs['urls']

        NewsContent.objects.filter(web_resource_name=source_from).delete()
        for i in range(0, len(titles)):
            news_content = NewsContent()
            news_content.web_resource_name = source_from
            news_content.post_name_title = titles[i]
            news_content.post_ulr = urls[i]
            news_content.save()


@background()
def collect_data():

    titles, urls = get_dou_news()
    NewsContent.store_to_db('DOU', titles=titles, urls=urls)

    titles, urls = get_itc_news()
    NewsContent.store_to_db('ITC', titles=titles, urls=urls)

    titles, urls = get_liga_news()
    NewsContent.store_to_db('LIGA', titles=titles, urls=urls)

