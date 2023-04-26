from django.contrib import admin
from .models import FAQS


# Register your models here.
class FAQSAdmin(admin.ModelAdmin):
    list_display = ['question', 'updated_at']
    date_hierarchy = 'updated_at'
    search_fields = ['question']


admin.site.register(FAQS, FAQSAdmin)
