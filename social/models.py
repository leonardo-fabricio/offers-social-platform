from django.db import models
from django.conf import settings

class Follow(models.Model):
    follower = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="following",
    )
    following = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="followers",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["follower", "following"],
                name="unique_follower_following",
            )
        ]

    def __str__(self) -> str:
        return f"{self.follower} → {self.following}"
