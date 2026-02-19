from django.contrib import admin

from .models import Collection, Favorite


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "user", "is_public", "created_at")
    list_filter = ("is_public", "created_at")
    search_fields = ("name", "user__username")


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "offer", "collection", "created_at")
    list_filter = ("created_at",)
    search_fields = ("user__username", "offer__title")
