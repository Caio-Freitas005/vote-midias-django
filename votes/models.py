from django.db import models
from django.contrib.auth.models import User
from medias.models import Media


class Vote(models.Model):
    VOTE_CHOICES = [
        (1, "Like"),
        (0, "Dislike"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    media = models.ForeignKey(Media, on_delete=models.CASCADE)
    vote_type = models.IntegerField(choices=VOTE_CHOICES)
    voted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "media")
        ordering = ["-id"]
