from django.contrib import admin

from django.contrib.flatpages.models import FlatPage
from django.contrib.flatpages.admin import FlatPageAdmin

from django.db import models

from ckeditor.widgets import CKEditorWidget

from .models import *


admin.site.unregister(FlatPage)
class FlatPageCustom(FlatPageAdmin):
    formfield_overrides = {models.TextField: {'widget': CKEditorWidget}}
admin.site.register(FlatPage, FlatPageCustom)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    class Meta:
        model = Category
admin.site.register(Category, CategoryAdmin)


class AdArchiveAdmin(admin.ModelAdmin):
    class Meta:
        model = AdArchive
admin.site.register(AdArchive, AdArchiveAdmin)




class TagAdmin(admin.ModelAdmin):
    class Meta:
        model = Tag
admin.site.register(Tag, TagAdmin)


class SellerAdmin(admin.ModelAdmin):
    class Meta:
        model = Seller
admin.site.register(Seller, SellerAdmin)



class StuffAdmin(admin.ModelAdmin):
    class Meta:
        model = Stuff
admin.site.register(Stuff, StuffAdmin)


class TypeFuelAdmin(admin.ModelAdmin):
    class Meta:
        model = TypeFuel
admin.site.register(TypeFuel, TypeFuelAdmin)


class CarAdmin(admin.ModelAdmin):
    class Meta:
        model = Car
admin.site.register(Car, CarAdmin)


class ServicesAdmin(admin.ModelAdmin):
    class Meta:
        model = Services
admin.site.register(Services, ServicesAdmin)

