from django import forms
from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import AdministratorMember, Banner


@admin.register(AdministratorMember)
class AdministratorMember(admin.ModelAdmin):
    readonly_fields = ["preview"]
    list_display = ("preview", "fio", "job_title", "bio")

    def preview(self, obj):
        return mark_safe(
            f'<img src="{obj.image.url}" style="max-height: 200px">')

    preview.short_description = "Изображение"


class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = '__all__'
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'file-input'}),
        }

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    form = BannerForm
    list_display = ('id', 'image_tag',)
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        return format_html('<img src="{}" style="max-width: 200px; max-height: 200px;"/>'.format(obj.image.url))

    image_tag.short_description = 'Изображение'