from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from .models import Doctor, TypeDoctor, RateDoctor, AdviceTime


class TypeDoctorAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'name',)


class DoctorAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'full_name', 'description',)


admin.site.register(Doctor, DoctorAdmin)
admin.site.register(TypeDoctor, TypeDoctorAdmin)
admin.site.register(RateDoctor)
admin.site.register(AdviceTime)


# Register your models here.
