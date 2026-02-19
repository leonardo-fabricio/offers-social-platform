from django.contrib import admin
from .models import Feed


@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "actor", "offer",
                    "action_type", "created_at")
    list_filter = ("action_type", "created_at")
    search_fields = ("user__username", "actor__username", "offer__title")
