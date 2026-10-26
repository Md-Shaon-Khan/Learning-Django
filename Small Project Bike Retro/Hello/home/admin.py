from django.contrib import admin
from home.models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'inquiry_type', 'phone', 'date')
    search_fields = ('name', 'email', 'bike_details')
    list_filter = ('inquiry_type', 'date')

admin.site.register(Contact, ContactAdmin)