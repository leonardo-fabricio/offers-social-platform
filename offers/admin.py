from django.contrib import admin
from .models import Offer


@admin.register(Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price", "created_by",
                    "favorites_count", "created_at")
    list_filter = ("created_by", "created_at")
    search_fields = ("title", "description")
