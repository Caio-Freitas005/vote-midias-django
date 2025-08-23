from django.contrib import admin
from .models import Media


class MediaAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "genre", "description", "image"]
    search_fields = ["title", "genre"]


admin.site.register(Media, MediaAdmin)
