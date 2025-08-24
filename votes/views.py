from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import Media, Vote


@login_required
@require_POST
def vote_media(request, media_id):
    media = Media.objects.get(id=media_id)
    vote_type = int(request.POST.get("vote_type"))

    Vote.register_vote(request.user, media, vote_type)

    # Retorna os contadores atualizados
    likes = Vote.objects.filter(media=media, vote_type=1).count()
    dislikes = Vote.objects.filter(media=media, vote_type=0).count()

    return JsonResponse({"likes": likes, "dislikes": dislikes})
