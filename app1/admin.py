from django.contrib import admin
from app1.models import EmployeeModel
from import_export.admin import ImportExportModelAdmin


@admin.register(EmployeeModel)
class ViewAdmin(ImportExportModelAdmin):#using import-export model to save data from exel or tsv file into database
    pass

