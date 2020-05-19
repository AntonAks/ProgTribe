from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):

    context_data = {
        "author1": 'User Name',
        "author2": 'User Name',
        "author3": 'User Name',
        "author4": 'User Name',
        }

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context["context_data"] = self.context_data
        return context

    template_name = 'home.html'


class IndexPageView(TemplateView):
    template_name = 'home.html'


class BlogPageView(TemplateView):
    template_name = 'blog/blog_page.html'
