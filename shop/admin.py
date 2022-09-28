from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin
from .models import Medicine, TypeMedicine, OrderModel, CartModel, PicturesMedicine, Advertising


class TypeMedicineAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'name',)


class MedicineAdmin(TabbedTranslationAdmin):
    list_display = ('id', 'name', 'title', )


admin.site.register(Medicine, MedicineAdmin)
admin.site.register(TypeMedicine, TypeMedicineAdmin)
admin.site.register(OrderModel)
admin.site.register(Advertising)
admin.site.register(CartModel)
admin.site.register(PicturesMedicine)

# Register your models here.
