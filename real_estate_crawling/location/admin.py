from django.contrib import admin
from .models import Offer, UserAgent
from django.utils.html import format_html

class OfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'description', 'url', 'area', 'address', 'source', 'last_change')
    list_display_editable = ('address', 'area')
    list_per_page = 20
    search_field =('title', 'description', 'address', 'area')
    # list_filter = ()

    def url(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.url)

admin.site.register(Offer, OfferAdmin)
