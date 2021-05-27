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
    class Meta:
        model = Category

admin.site.register(Category, CategoryAdmin)


class AdAdmin(admin.ModelAdmin):
    class Meta:
        model = Ad

admin.site.register(Ad, AdAdmin)


class TagAdmin(admin.ModelAdmin):
    class Meta:
        model = Tag

admin.site.register(Tag, TagAdmin)


class SellerAdmin(admin.ModelAdmin):
    class Meta:
        model = Seller

admin.site.register(Seller, SellerAdmin)
