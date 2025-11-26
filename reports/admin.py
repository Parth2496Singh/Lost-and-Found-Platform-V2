from django.contrib import admin
from .models import LostItems, FoundItem

# Register your models here.
admin.site.register(LostItems)
admin.site.register(FoundItem)