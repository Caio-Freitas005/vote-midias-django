from django.urls import path
from . import views

app_name = "medias"
urlpatterns = [
    path("", views.MediasView.as_view(), name="medias"),
]
