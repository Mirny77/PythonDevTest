
from django.contrib import admin
from .models import *
from import_export.admin import ImportExportActionModelAdmin
from import_export import resources,fields
from import_export.widgets import ForeignKeyWidget


class NewContactResourse(resources.ModelResource):


    class Meta:
        model = NewContact

class NewContactAdmin(ImportExportActionModelAdmin):
    list_display = [field.name for field in NewContact._meta.fields]
    resource_class = NewContactResourse
admin.site.register(NewContact, NewContactAdmin)
# class NewContactAdmin (admin.ModelAdmin):
# #     list_display = [field.name for field in NewContact._meta.fields]
# #
# #     class Meta:
# #         model = NewContact
# #
# #

class CompanyAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Company._meta.fields]

    class Meta:
        model = Company

admin.site.register(Company, CompanyAdmin)