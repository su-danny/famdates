from django.contrib import admin
from contact_form.models import Contact, ContactCategory


class ContactAdmin(admin.ModelAdmin):
    list_display = ('created', 'name', 'email')


class ContactCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')


admin.site.register(Contact, ContactAdmin)
admin.site.register(ContactCategory, ContactCategoryAdmin)
