from django.contrib import admin
from .models import Vote


class VoteAdmin(admin.ModelAdmin):
    list_display = ["user", "media", "vote_type", "voted_at"]
    search_fields = ["user", "media", "vote_type"]
    list_filter = ["voted_at", "vote_type"]


admin.site.register(Vote, VoteAdmin)
