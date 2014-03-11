from django.contrib import admin
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail
from notification.models import *
from datetime import datetime


class NotificationTemplateContentInline(admin.TabularInline):
    model = NotificationTemplateContent


class NotificationTemplateAdmin(admin.ModelAdmin):
    list_filter = ('name', )
    inlines = [NotificationTemplateContentInline]


class NotificationAdmin(admin.ModelAdmin):
    model = Notification
    list_display = ('subject', 'is_sent', 'recipients')


admin.site.register(NotificationTemplate, NotificationTemplateAdmin)
admin.site.register(Notification, NotificationAdmin)