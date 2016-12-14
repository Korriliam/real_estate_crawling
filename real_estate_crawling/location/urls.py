from django.conf.urls import url
from django.contrib import admin
import views

urlpatterns = [
    url(r'^admin/?', admin.site.urls),
    url(r'^$', 'location.views.index'),
]
