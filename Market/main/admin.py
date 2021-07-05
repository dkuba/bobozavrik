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
    list_display = ('id', 'email', 'username', )
    list_display_links = ('id', 'email', 'username',)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

    class Meta:
        model = Category


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'publication',)
    list_display_links = ('id', 'title',)
    list_filter = ("tag",'created_date', )  # add filters for model Car in admin panel

    list_editable = ('publication',)
    actions = ["publish", "unpublish"]

    # add new actions - publish / unpublish
    def unpublish(self, request, queryset):
        """Снять с публикации"""
        row_update = queryset.update(publication=False)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f"{message_bit}")


    def publish(self, request, queryset):
        """Опубликовать"""
        row_update = queryset.update(publication=True)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f"{message_bit}")

    publish.short_description = "Опубликовать"
    unpublish.short_description = "Снять с публикации"


admin.site.register(Category, CategoryAdmin)
admin.site.register(AdArchive)
admin.site.register(Tag)
admin.site.register(Stuff)
admin.site.register(TypeFuel)
admin.site.register(Services)
admin.site.register(Picture)
admin.site.register(Profile)
admin.site.register(Subscriber)
admin.site.register(SMSLog)
