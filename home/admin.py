from django.contrib import admin
from .models import Reported


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(Reported, ProductAdmin)
