from django.contrib import admin
from .models import Offer, UserAgent
from django.utils.html import format_html
from django.contrib.admin import RelatedFieldListFilter

class OfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'description', 'url', 'area', 'address', 'source', 'last_change')
    list_display_editable = ('area', )
    list_per_page = 30
    search_fields =('title', 'description', 'area', )
    list_filter = (
        ('source', RelatedOnlyFieldListFilter),
        ('offer_category', RelatedOnlyFieldListFilter),
    )
    def show_url(self, obj):
        return format_html("<a href='{url}'>{url}</a>", url=obj.url)
    show_url.allow_tags = True

admin.site.register(Offer, OfferAdmin)