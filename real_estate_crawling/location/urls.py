from django.conf.urls import url
from django.contrib import admin
from .views import index
import views

urlpatterns = [
    url(r'^admin/?', admin.site.urls),
    url(r'^$', index),
]
