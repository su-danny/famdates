# -*- coding: utf-8 -*-

from django.contrib import admin

from models import UserProfile, Interest, InterestCategory, InterestGroup, Child

class InterestAdmin(admin.ModelAdmin):
    search_fields = ['name']

class ChildInline(admin.TabularInline):
    model = Child

class UserProfileAdmin(admin.ModelAdmin):
    inlines = [
        ChildInline,
    ]

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register([InterestCategory, Child])
admin.site.register(Interest, InterestAdmin)
admin.site.register(InterestGroup)
