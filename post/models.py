from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from picklefield.fields import PickledObjectField
from famdates.fileupload.models import MediaFile


class Location(models.Model):
    """Point model."""
    latitude = models.FloatField(_('latitude'), blank=True, null=True)
    longitude = models.FloatField(_('longitude'), blank=True, null=True)
    address = models.CharField(_('address'), max_length=200, blank=True)
    city = models.CharField(_('city'), max_length=200, blank=True)
    zipcode = models.CharField(_('zip'), max_length=10, blank=True)
    country = models.CharField(_('country'), blank=True, max_length=100)

    class Meta:
        verbose_name = _('Location')
        verbose_name_plural = _('Locations')
        db_table = 'post_location'
        ordering = ('address',)

    def __unicode__(self):
        return u'%s' % self.address


class Post(models.Model):
    body = models.CharField(max_length=1000, default='')
    author = models.ForeignKey(User, null=True, blank=True)
    wall = models.ForeignKey(User, null=True, blank=True, related_name='wall_posts')
    created = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    default_image = models.ImageField(upload_to='post', blank=True, null=True)
    video = models.FileField(upload_to='video', blank=True, null=True)
    youtube_id = models.CharField(max_length=50, null=True, blank=True)
    feed = models.CharField(max_length=50, null=True, blank=True)
    is_sticky = models.BooleanField(default=False)
    media = models.ManyToManyField(MediaFile, blank=True, null=True)

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
        db_table = 'post_post'
        ordering = ('-pk',)

    def __unicode__(self):
        return self.body

    def get_absolute_url(self):
        return ''

    def get_feed(self):
        return {'fan_zone': 'Fan Zone',
                'game_time': 'Game Time',
                'fitness_nutrition': 'Fitness & Nutrition'}.get(self.feed)

    def save(self):
        from common.utils import ireplace

        if self.body:
            body = self.body.lower()

            if '#getfit' in body:
                self.feed = "fitness_nutrition"
                self.body = ireplace('#getfit', '', self.body)
            elif '#fanzone' in body:
                self.feed = "fan_zone"
                self.body = ireplace('#fanzone', '', self.body)
            elif '#gametime' in body:
                self.feed = 'game_time'
                self.body = ireplace('#gametime', '', self.body)

        super(Post, self).save()


class StickyClosedPost(models.Model):
    post = models.ForeignKey(Post)
    user = models.ForeignKey(User)


class Comment(models.Model):
    body = models.CharField(max_length=1000, default='')
    author = models.ForeignKey(User, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, related_name='comments')


class MediaPost(models.Model):
    post = models.ForeignKey(Post)
    media = models.ForeignKey(MediaFile)
    
    
    
    
    