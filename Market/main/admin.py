from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from .models import *


admin.site.unregister(FlatPage)


class FlatPageAdmin(admin.ModelAdmin):
    content = RichTextUploadingField()
    class Meta:
        model = FlatPage

admin.site.register(FlatPage, FlatPageAdmin)

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
