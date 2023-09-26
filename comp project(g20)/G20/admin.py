from django.contrib import admin
from .models import Item

class TopicItemAdmin(admin.ModelAdmin):
    list_display = ('Topic', 'description')
    search_fields = ('Topic', 'description')



admin.site.register(Item ,TopicItemAdmin)