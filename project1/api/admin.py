from dataclasses import fields
from pyexpat import model
from django.contrib import admin
from .models import Item
# Register your models here.

class ItemAdmin(admin.ModelAdmin):
        list_display = ('name', 'price', 'description')

admin.site.register(Item,ItemAdmin)