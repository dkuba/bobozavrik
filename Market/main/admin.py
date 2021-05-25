from django.contrib import admin
from django.contrib.flatpages.models import FlatPage
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


admin.site.unregister(FlatPage)


class FlatPageAdmin(admin.ModelAdmin):
    content = RichTextUploadingField()
    class Meta:
        model = FlatPage

admin.site.register(FlatPage, FlatPageAdmin)

