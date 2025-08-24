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

    @classmethod
    def register_vote(cls, user, media, vote_type):
        vote, created = cls.objects.get_or_create(user=user, media=media)
        if not created:
            if vote.vote_type == vote_type:
                vote.delete()
                return False  # Voto removido
            else:
                vote.vote_type = vote_type
                vote.save()
        else:
            vote.vote_type = vote_type
            vote.save()
        return True  # Voto registrado ou atualizado
