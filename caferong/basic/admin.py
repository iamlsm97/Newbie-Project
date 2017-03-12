from django.contrib import admin
from basic.models import Cafe

# Register your models here.
class CafeAdmin(admin.ModelAdmin):
    list_display = ("name", "time", "locLat", "locLng", "Roastery", "Engname")
    list_filter = ("name",)

admin.site.register(Cafe, CafeAdmin)

