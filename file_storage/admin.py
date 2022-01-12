from django.contrib import admin

from .models import UserDocuments


class UserDocumentsAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'name', 'file_size', 'ext', 'file'
    )
    fields = ['user', 'file']

    def file_size(self, obj):
        return f'{int(obj.size/1024)}K'

    file_size.short_description = 'SIZE'
    file_size.allow_tags = True

    def save_model(self, request, obj, form, change):
        file_name = obj.file.name
        obj.name = file_name
        obj.size = obj.file.size
        obj.ext = file_name[file_name.rindex('.') + 1:] if '.' in file_name else ''
        obj.save()


admin.site.register(UserDocuments, UserDocumentsAdmin)
