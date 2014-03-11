from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.utils.translation import ugettext as _
from django.conf import settings

from itertools import islice, takewhile
from datetime import datetime
from dateutil import rrule
#from famdates.account.models import Interest, InterestCategory
from durationfield.db.models.fields.duration import DurationField

frecuencies = (
    (-1, _('Single time')),
    (rrule.DAILY, _('Daily')),
    (rrule.WEEKLY, _('Weekly')),
    (rrule.MONTHLY, _('Montly')),
    (rrule.YEARLY, _('Yearly')),
)

MAX_PAST = getattr(settings, 'EVENTS_MAX_PAST_OCCURRENCES', None)
MAX_FUTURE = settings.EVENTS_MAX_FUTURE_OCCURRENCES


class Occurrence(models.Model):
    datetime = models.DateTimeField()
    event = models.ForeignKey('Event')

    def __unicode__(self):
        return unicode(self.datetime)


class Event(models.Model):
    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')

    name = models.TextField(_('Event Name'), default='Unknown Event')
    PUBLIC = 'pub'
    PERSONAL = 'per'
    beginning = models.DateField(_('Beginning'))
    time = models.TimeField(_('Time'))
    duration = DurationField(_('Duration'))
    details = models.TextField(_('Details'))
    TYPE_CHOICE = (
        (PUBLIC, 'PUBLIC'),
        (PERSONAL, 'PERSONAL'),
    )
    type = models.CharField(max_length=3,
                            choices=TYPE_CHOICE,
                            default=PUBLIC)
    interests = models.ManyToManyField('account.Interest') #, null=True, blank=True)
    interval = models.PositiveSmallIntegerField(_('Interval'), default=1,
                                                help_text=_('Interval between frequency'), null=True, blank=True)

    frequency = models.SmallIntegerField(_('Frequency'), choices=frecuencies,
                                         default=-1, null=True, blank=True)

    repetitions = models.PositiveSmallIntegerField(_('Maximum repetitions'),
                                                   blank=True, null=True, help_text=_('Endless if not defined'))

    end = models.DateTimeField(_('Maximum date'), blank=True, null=True,
                               help_text=_('Endless if not defined'))

    content_type = models.ForeignKey(ContentType, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    related_object = generic.GenericForeignKey('content_type', 'object_id')

    def __unicode__(self):
        return '%s %s %s' % (unicode(self.beginning), unicode(self.time),
                             self.get_frequency_display())

    def start_datetime(self):
        return datetime.combine(self.beginning, self.time)

    def get_occurrences(self):
        if self.frequency is -1:
            return datetime.combine(self.beginning, self.time),
        return rrule.rrule(
            self.frequency,
            dtstart=datetime.combine(self.beginning, self.time),
            interval=self.interval,
            count=self.repetitions,
            until=self.end,
        )

    def get_past_occurrences(self, num=None):
        past = list(takewhile(
            lambda occurrence: occurrence < datetime.now(),
            self.get_occurrences(),
        ))
        if num:
            return past[:-num:-1]
        return past[::-1]

    def get_future_occurrences(self, num):
        future = ( occurrence for occurrence in self.get_occurrences() \
                   if occurrence > datetime.now() )
        return list(islice(future, None, num))

    def update_occurrences_set(self, occurrences):
        #delete old ones
        for occurrence in self.occurrence_set.exclude(datetime__in=occurrences):
            occurrence.delete()
            #add new ones
        for occurrence in occurrences:
            if not self.occurrence_set.filter(datetime=occurrence):
                Occurrence(datetime=occurrence, event=self).save()

    # def save(self, *args, **kwargs):
    #     if self.repetitions or self.end:
    #         occurrences = self.get_occurrences()
    #     else:
    #         occurrences = self.get_past_occurrences(MAX_PAST) + \
    #                       self.get_future_occurrences(MAX_FUTURE)
    #
    #     super(Event, self).save(*args, **kwargs)
    #     self.update_occurrences_set(occurrences)

    def delete(self, *args, **kwargs):
        for occurrence in self.occurrence_set.all():
            occurrence.delete()
        super(Event, self).delete(*args, **kwargs)



"""
from django.conf import settings

from djangogcal.adapter import CalendarAdapter, CalendarEventData
from djangogcal.observer import CalendarObserver


class ShowingCalendarAdapter(CalendarAdapter):
    def get_event_data(self, instance):
        return CalendarEventData(
            start=instance.start_time,
            end=instance.end_time,
            title=instance.title
        )

observer = CalendarObserver(email=settings.CALENDAR_EMAIL,
                            password=settings.CALENDAR_PASSWORD)
observer.observe(Event, ShowingCalendarAdapter())
"""