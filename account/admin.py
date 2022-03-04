from django.contrib import admin
from .models import UserModel, CountyModel, RegionModel
from modeltranslation.admin import TabbedTranslationAdmin
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    # add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    model = UserModel
    list_display = ('username', 'is_staff', 'is_active',)
    list_filter = ('username', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'password', 'first_name', 'last_name', 'email', 'avatar', 'address', 'language',
                'favorite_medicine', 'favorite_doctor', 'theme_mode', 'specialist_doctor')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'password1', 'password2',
                       'is_staff',
                       'is_active')}
         ),
    )
    search_fields = ('username',)
    ordering = ('username',)


class CountryAdmin(TabbedTranslationAdmin):
    list_display = ['name']


class RegionAdmin(TabbedTranslationAdmin):
    list_display = ['name']


admin.site.register(UserModel, CustomUserAdmin)
admin.site.register(CountyModel, CountryAdmin)
admin.site.register(RegionModel, RegionAdmin)

