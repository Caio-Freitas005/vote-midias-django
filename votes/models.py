from django.db import models, transaction
from django.db.models import F
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
    @transaction.atomic
    def register_vote(cls, user, media, vote_type):
        vote, created = cls.objects.get_or_create(
            user=user, media=media, defaults={"vote_type": vote_type}
        )

        if created:
            # Novo voto, apenas incrementa o contador correto
            if vote_type == 1:
                media.likes = F("likes") + 1
            else:
                media.dislikes = F("dislikes") + 1
        else:
            # O voto já existe
            if vote.vote_type == vote_type:
                # O usuário clicou no mesmo botão (like -> like), então remove o voto
                if vote_type == 1:
                    media.likes = F("likes") - 1
                else:
                    media.dislikes = F("dislikes") - 1
                vote.delete()
            else:
                # O usuário mudou o voto (like -> dislike ou dislike -> like)
                if vote_type == 1:  # Era dislike, virou like
                    media.likes = F("likes") + 1
                    media.dislikes = F("dislikes") - 1
                else:  # Era like, virou dislike
                    media.likes = F("likes") - 1
                    media.dislikes = F("dislikes") + 1
                vote.vote_type = vote_type
                vote.save()

        media.save()
        media.refresh_from_db()  # Atualiza o objeto media com os novos valores do banco
        return media.likes, media.dislikes
