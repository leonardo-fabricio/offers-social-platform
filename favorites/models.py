from django.db import models
from django.conf import settings
from offers.models import Offer


class Collection(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="collections",
    )
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.name} ({self.user})"


class Favorite(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="favorites",
    )
    offer = models.ForeignKey(
        Offer,
        on_delete=models.CASCADE,
        related_name="favorites",
    )
    collection = models.ForeignKey(
        Collection,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="favorites",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "offer"], name="unique_favorite_per_user_offer"
            )
        ]

    def __str__(self) -> str:
        return f"{self.user} → {self.offer}"
