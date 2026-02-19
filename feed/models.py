from django.db import models
from django.conf import settings
from offers.models import Offer

class Feed(models.Model):
    ACTION_FAVORITE = "FAVORITE"
    ACTION_CREATED = "CREATED"
    ACTION_CHOICES = [
        (ACTION_FAVORITE, "Favorite"),
        (ACTION_CREATED, "Created"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="feed_entries",
    )  # quem vê o feed
    actor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="feed_actions",
    )  # quem gerou ação
    offer = models.ForeignKey(
        Offer,
        on_delete=models.CASCADE,
        related_name="feed_entries",
    )
    action_type = models.CharField(
        max_length=20,
        choices=ACTION_CHOICES,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.actor} {self.action_type} {self.offer} for {self.user}"
