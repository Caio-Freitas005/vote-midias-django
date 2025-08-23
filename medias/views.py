from django.shortcuts import render
from django.views import generic
from .models import Media


class MediasView(generic.ListView):
    template_name = "medias/medias.html"
    context_object_name = "medias_list"

    def get_queryset(self):
        return Media.objects.all()
