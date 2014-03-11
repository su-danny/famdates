from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from static_page.forms import StaticpageForm, StaticpageContentForm
from static_page.models import *


class StaticContentInline(admin.TabularInline):
    model = StaticContent
    #    form = StaticpageContentForm
    max_num = 1


class LinkInline(admin.TabularInline):
    model = Link


class StaticPageAdmin(admin.ModelAdmin):
    form = StaticpageForm
    fieldsets = (
        (None, {'fields': ('url', 'name', 'sites', 'parent', 'order')}),
        (_('Advanced options'),
         {'classes': ('collapse',), 'fields': ('enable_comments', 'registration_required', 'template_name')}),
    )
    list_display = ('url', 'name')
    list_filter = ('sites', 'enable_comments', 'registration_required')
    search_fields = ('url', 'name')
    inlines = [StaticContentInline, LinkInline, ]


admin.site.register(StaticPage, StaticPageAdmin)
