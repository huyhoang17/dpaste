from django.contrib import admin

from dpaste.models import Snippet


class SnippetAdmin(admin.ModelAdmin):
    list_display = ('secret_id', 'content', 'published', 'view_count')


admin.site.register(Snippet, SnippetAdmin)
