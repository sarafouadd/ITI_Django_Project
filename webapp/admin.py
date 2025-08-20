from django.contrib import admin
from .models import *


@admin.register(Category)
class categoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    pass