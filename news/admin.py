from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from .models import NewsModel, TagsModel


class NewsAdmin(TabbedTranslationAdmin):
    list_display = ('name', 'description',)


class TagsAdmin(TabbedTranslationAdmin):
    list_display = ('tag_name',)


admin.site.register(NewsModel, NewsAdmin)
admin.site.register(TagsModel, TagsAdmin)

