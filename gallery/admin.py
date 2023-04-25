from django.contrib import admin

from .models import Gallery


class GalleryModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']
    search_fields = ['title']


admin.site.register(Gallery, GalleryModelAdmin)
