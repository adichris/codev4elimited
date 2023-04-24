from django.contrib import admin
from .models import Service, ServicesContent


class ServicesContentAdminInline(admin.StackedInline):
    model = ServicesContent


class ServicesModelAdmin(admin.ModelAdmin):
    list_display = ['headline', 'flyer', 'featured']
    search_fields = ['headline']
    readonly_fields = ['slug']
    inlines = [ServicesContentAdminInline]


admin.site.register(Service, ServicesModelAdmin)
