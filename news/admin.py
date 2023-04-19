from admin_auto_filters.filters import AutocompleteFilter

from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from .models import NewsModel, TagsModel, Advertising, Notification


class HashTagFilter(AutocompleteFilter):
    title = "Hash tag"
    field_name = 'hashtag'


class MedicineFilter(AutocompleteFilter):
    title = "Medicine"
    field_name = 'medicine'


class DoctorFilter(AutocompleteFilter):
    title = "Doctor"
    field_name = 'doctor'


class NewsModelAdmin(TabbedTranslationAdmin):
    date_hierarchy = 'created_at'
    list_display = ('id', 'image', 'name', 'hashtag', 'description', 'created_at', )
    list_filter = [HashTagFilter, ]
    search_fields = ['id', 'name', 'description', ]
    autocomplete_fields = ['hashtag', ]


class TagsModelAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'tag_name', )
    search_fields = ['id', 'tag_name', ]


class AdvertisingAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'title', 'text', 'medicine', 'doctor', 'type', ]
    list_filter = [MedicineFilter, DoctorFilter, 'type', ]
    search_fields = ['id', 'title', 'text', ]
    autocomplete_fields = ['medicine', 'doctor', ]


class NotificationAdmin(admin.ModelAdmin):
    date_hierarchy = 'push_time'
    list_display = ['id', 'title', 'description', 'image', 'foreign_id', 'type', 'push_time', ]
    list_filter = ['type', ]
    search_fields = ['id', 'title', 'description', 'foreign_id', ]


admin.site.register(NewsModel, NewsModelAdmin)
admin.site.register(TagsModel, TagsModelAdmin)
admin.site.register(Advertising, AdvertisingAdmin)
admin.site.register(Notification, NotificationAdmin)



