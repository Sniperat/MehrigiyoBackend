from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from .models import NewsModel


class NewsAdmin(TabbedTranslationAdmin):
    list_display = ('name', 'description',)


admin.site.register(NewsModel, NewsAdmin)

