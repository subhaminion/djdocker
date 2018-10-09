from django.conf.urls import url
from django.contrib import admin
from main.views import (
    index, init_csv
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^init_csv/', init_csv),
    url(r'^(?P<key>\w{0,50})/$', index),
]
