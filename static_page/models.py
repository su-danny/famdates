from django.db import models
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


class StaticPage(models.Model):
    url = models.CharField(_('URL'), max_length=100, db_index=True)
    name = models.CharField(_('page name'), max_length=200)
    enable_comments = models.BooleanField(_('enable comments'))
    template_name = models.CharField(_('template name'), max_length=70, blank=True,
                                     help_text=_(
                                         "Example: 'flatpages/contact_page.html'. If this isn't provided, the system will use 'flatpages/default.html'."))
    registration_required = models.BooleanField(_('registration required'), help_text=_(
        "If this is checked, only logged-in users will be able to view the page."))

    parent = models.ForeignKey('StaticPage', blank=True, null=True, related_name='children')

    order = models.PositiveIntegerField(blank=True, null=True)

    sites = models.ManyToManyField(Site)

    class Meta:
        verbose_name = _('static page')
        verbose_name_plural = _('statics pages')
        ordering = ('name',)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return self.url


class StaticContent(models.Model):
    title = models.CharField(_('title'), max_length=200)
    content = models.TextField(_('content'), blank=True)
    language = models.CharField(_('language'), max_length=10, choices=settings.LANGUAGES)
    static_page = models.ForeignKey(StaticPage, related_name='contents')


class Link(models.Model):
    name = models.CharField(max_length=200)
    static_page = models.ForeignKey(StaticPage)

    def __unicode__(self):
        return self.name