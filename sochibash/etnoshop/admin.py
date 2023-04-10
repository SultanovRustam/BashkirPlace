from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Product, Review


class ProductAdmin(admin.ModelAdmin):
    list_display = ('preview', 'name', 'price', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')
    readonly_fields = ["preview"]
    ordering = ('-price',)

    def preview(self, obj):
        return mark_safe(
            f'<img src="{obj.image.url}" style="max-height: 200px;">')

    preview.short_description = "Изображение"


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'author', 'rating')
    list_filter = ('product',)
    search_fields = ('author', 'text')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
