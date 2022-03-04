from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from .models import Medicine, TypeMedicine


class TypeMedicineAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'name',)


class MedicineAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'name', 'title', )


admin.site.register(Medicine, MedicineAdmin)
admin.site.register(TypeMedicine, TypeMedicineAdmin)

# Register your models here.
