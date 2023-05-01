from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Comment, Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ["preview"]
    list_display = ("preview", "fio", "age",
                    "family_status", "children",
                    "activity", "bio", "phone_number")

    def preview(self, obj):
        return mark_safe(
            f'<img src="{obj.image.url}" style="max-height: 200px;">')

    preview.short_description = "Изображение"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("author", "profile", "pub_date", "text")
