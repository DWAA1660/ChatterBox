from django.conf.urls import url
from django.contrib import admin
from example_app.views import ChatterBoxAppView, ChatterBoxApiView


urlpatterns = [
    url(r'^$', ChatterBoxAppView.as_view(), name='main'),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^api/chatterbox/', ChatterBoxApiView.as_view(), name='chatterbox'),
]
