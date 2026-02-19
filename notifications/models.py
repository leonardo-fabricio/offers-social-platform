from django.db import models
from django.conf import settings

class Notification(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notifications",
    )  # quem recebe
    actor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notifications_sent",
    )  # quem gerou
    type = models.CharField(max_length=50)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"Notification to {self.user} from {self.actor} ({self.type})"
