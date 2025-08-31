from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from medias.models import Media
from .models import Vote


@login_required
@require_POST
def vote_media(request, media_id):
    media = get_object_or_404(Media, id=media_id)
    vote_type_str = request.POST.get("vote_type")

    if vote_type_str not in ["like", "dislike"]:
        return HttpResponseBadRequest("Tipo de voto inválido.")

    vote_type = 1 if vote_type_str == "like" else 0

    likes, dislikes = Vote.register_vote(request.user, media, vote_type)

    return JsonResponse({"likes": likes, "dislikes": dislikes})
