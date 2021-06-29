from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin
from django.db import models
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.models import User
from .models import (Tag, Stuff, Category, SMSLog, Subscriber,
                    AdArchive, TypeFuel, Car, Services, Profile, Picture)


admin.site.unregister(FlatPage)


class FlatPageCustom(FlatPageAdmin):
    formfield_overrides = {models.TextField: {'widget': CKEditorWidget}}


admin.site.register(FlatPage, FlatPageCustom)


# Ad user-id in admin
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'username',)
    list_display_links = ('id', 'email', 'username',)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

    class Meta:
        model = Category


admin.site.register(Category, CategoryAdmin)
admin.site.register(AdArchive)
admin.site.register(Tag)
admin.site.register(Stuff)
admin.site.register(TypeFuel)
admin.site.register(Car)
admin.site.register(Services)
admin.site.register(Picture)
admin.site.register(Profile)
admin.site.register(Subscriber)
admin.site.register(SMSLog)
