
from django.contrib import admin
from django.urls import path
from .views import HomePageView, IndexPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('index/', IndexPageView.as_view(), name='index'),

]
