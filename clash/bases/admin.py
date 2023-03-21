from django.contrib import admin

from clash.bases.models import TownhallSelection


# Register your models here.

@admin.register(TownhallSelection)
class TownhallAdmin(admin.ModelAdmin):
    pass