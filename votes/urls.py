from django.urls import path
from . import views

app_name="votes"
urlpatterns = [
    path("vote/<int:media_id>/", views.vote_media, name="vote_media")
]
