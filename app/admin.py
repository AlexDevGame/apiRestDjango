from django.contrib import admin
from django.utils.html import format_html
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','cover_thumbnail')

    def cover_thumbnail(self, obj):
        if obj.cover:
            return format_html('<img src="{}" style="max-height:100px;"/>'.format(obj.cover.url))
        return "-"
    cover_thumbnail.short_description = 'Cover'
