from django.contrib import admin
from .models import Offer, UserAgent


class OfferAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'description', 'url', 'area', 'address', 'source', 'last_change')
    list_display_editable = ('address', 'area')
    list_per_page = 20
    search_field =('title', 'description', 'address', 'area')
    # list_filter = ()

admin.site.register(Offer, OfferAdmin)
