# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.contenttypes import generic
from famdates.events.models import Event
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User, AnonymousUser
from django.db.models.signals import class_prepared
from famdates.follow import utils
from famdates.post.models import Post
from picklefield.fields import PickledObjectField
import datetime
from famdates.fileupload.models import MediaFile
from famdates.common.models import ABR_STATE_CHOICES
from famdates.follow.models import Follow

MALE, FEMALE = range(1, 3)
GENDER_CHOICES = (
    (MALE, u'Male'),
    (FEMALE, u'Female'),
)

GENDER = (('male', "Male"),
          ('female', "Female"))

STATUS = (('single', "Single"),
          ('married', "Married"))

ACCT_TYPES = (('individual', "Individual"),
              ('business', "Team or Business"))


def user_unicode(self):
    name = (self.first_name or '') + ' ' + (self.last_name or '')
    return name.strip() or self.username


User.__unicode__ = user_unicode


class InterestCategory(models.Model):
    name = models.CharField(max_length=100)
    human_name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.human_name

    def get_normalized_name(self):
        if self.name == "fitness_nutrition": return 'getfit'
        elif self.name == "game_time": return 'gametime'
        elif self.name == "fan_zone": return 'fanzone'

        return ''

class InterestGroup(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Interest(models.Model):
    category = models.ForeignKey(InterestCategory)
    sub_category = models.CharField(max_length=100, blank=True, null=True)
    group = models.ForeignKey(InterestGroup, blank=True, null=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True, upload_to='uploads/interests', verbose_name="Interest Image")

    def __unicode__(self):
        return self.name

    def get_thumb(self):
        if not self.image:
            return '/static/images/weight-lift.png'
        else:
            return '/media' +  self.image

    """
        Returns fanzone, getfit, gametime or ''
    """
    def get_type(self):
        if self.category:
            return self.category.get_normalized_name()

        return ''

EMAIL_NOTIFICATIONS = (('enabled', "Enable Email Notification"),
                       ('disabled', "Disable Email notification"))


class SimilarProfileManager(models.Manager):
    def other_profiles(self, user):
        """
        Returns all messages that were received by the given user and are not
        marked as deleted.
        """
        return self.exclude(user=user).filter(
            deactivated=False,
            is_private=False
        )

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True, related_name='user_profile')
    avatar = models.ImageField(blank=True, null=True, upload_to='uploads/avatars', verbose_name="Profile Image")
    gender = models.CharField(choices=GENDER, max_length=10, verbose_name="I am", blank=True, null=True)
    acct_type = models.CharField(max_length=50, choices=ACCT_TYPES, help_text="", blank=True, null=True,
                                 verbose_name="Account Type")

    region = models.CharField(max_length=200, verbose_name="I lived in", blank=True, null=True)
    about_me = models.TextField(blank=True, verbose_name="Tell Us About Yourself")
    city = models.CharField(max_length=100, verbose_name="City Name")
    state = models.CharField(max_length=100, verbose_name="State", choices=ABR_STATE_CHOICES)

    use_gravatar = models.BooleanField(default=False)
    hide_birthday = models.BooleanField(default=False)
    show_month_day = models.BooleanField(default=False)

    birthday = models.DateField(blank=True, null=True, help_text="Birthday")
    date_founded = models.DateField(blank=True, null=True, help_text="Date Founded")
    occupation = models.CharField(max_length=200, verbose_name="Occupation", blank=True, null=True)

    zipcode = models.CharField(max_length=5, null=True, blank=True)

    #add field for Business profile
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Phone")
    profile_type = models.CharField(max_length=20, blank=True, null=True, default='normal')
    facebook_uid = models.CharField(verbose_name=u'facebook id', max_length=30, blank=True)
    fan_zone_interests = models.ManyToManyField(Interest,
                                                blank=True,
                                                null=True,
                                                limit_choices_to={'category__name': 'fan_zone'},
                                                related_name='fan_zone')

    fitness_nutrition_interests = models.ManyToManyField(Interest,
                                                         blank=True,
                                                         null=True,
                                                         limit_choices_to={'category__name': 'fitness_nutrition'},
                                                         related_name='fitness_nutrition'
    )

    game_time_interests = models.ManyToManyField(Interest,
                                                 blank=True, null=True,
                                                 limit_choices_to={'category__name': 'game_time'},
                                                 related_name='game_time'
    )

    default_interest_feed = models.ForeignKey(InterestCategory, null=True, blank=True)
    email_notification = models.CharField(max_length=50, choices=EMAIL_NOTIFICATIONS, default='enabled')
    receive_email_from_groups = models.BooleanField('Receive email notification for groups I belong to', default=True)
    receive_email_for_new_message = models.BooleanField('Receive email notification for new direct message',
                                                        default=True)
    blocked_users = models.ManyToManyField(User, null=True, blank=True)

    deactivated = models.BooleanField(default=False)
    is_private = models.BooleanField(default=False)
    background = models.ImageField(blank=True, null=True, upload_to='uploads', verbose_name="Background Image")
    background_cropped = models.ImageField(blank=True, null=True, upload_to='uploads',
                                           verbose_name="Cropped Background Image")

    stats = PickledObjectField(null=True)
    address = models.CharField(max_length=200, verbose_name="Address", blank=True, null=True)
    attn = models.CharField(max_length=20, verbose_name="Attn", blank=True, null=True)

    objects = SimilarProfileManager()

    events = generic.GenericRelation(Event)
    joined_events = models.ManyToManyField(Event, through='EventJoin', null=True, blank=True, related_name="joined_userprofile")
    current_registration_step = models.CharField(max_length=20, null=True, blank=True)


    def __unicode__(self):
        return u'%s %s - %s' % (self.user.first_name, self.user.last_name, self.user.username)

    def get_pretty_name(self):
        return self.get_full_name

    def update_registration_step(self, step):
        self.current_registration_step = step
        self.save()

    def get_background(self):
        if self.background:
            return '/static/images/profile_header.png'
            #return '/media/' + str(self.background)
        else:
            return '/static/images/profile_header.png'

    def get_age(self):
        from datetime import date
        if not self.birthday:
            return 0

        today = date.today()

        try:
            birthday = self.birthday.replace(year=today.year)
        except ValueError: # raised when birth date is February 29 and the current year is not a leap year
            birthday = self.birthday.replace(year=today.year, day=born.day-1)
        if birthday > today:
            return today.year - self.birthday.year - 1
        else:
            return today.year - self.birthday.year

    @property
    def get_full_name(self):
        if hasattr(self.user, 'display_name') and self.user.display_name:
            name = self.user.display_name
        elif self.user.first_name and self.user.last_name:
            name = u'%s %s' % (self.user.first_name, self.user.last_name)
        else:
            name = self.user.email
        return name

    def get_interests(self):
        children = list(Child.objects.filter(parent_id=self.id))
        interests_id = []
        for child in children:
            if child.interest:
                for i in child.interest.all():
                    if i.id not in interests_id:
                        interests_id.append(i.id)
        return interests_id

    def get_interest_count(self):
        return self.fitness_nutrition_interests.all().count() + self.game_time_interests.all().count() + self.fan_zone_interests.all().count()

    @property
    def interests(self):
        return Interest.objects.filter(id__in=self.get_interests())

    def get_settings(self, param):
        return True

    def get_rate(self):
        return ['icon-star' for i in xrange(5)]

    def get_photo_count(self):
        return len(self.get_photos())

    def get_photos(self):
        return [media for media in MediaFile.objects.exclude(image__isnull=True).filter(post__author=self.user) if
                media.image]

    def get_following_profiles(self):
        return [follow.target_userprofile for follow in Follow.objects.filter(user=self.user).exclude(is_blocked=True)]

    def get_following_users(self):
        return [profile.user for profile in self.get_following_profiles()]

    def get_similar_profiles(self, group_by_category=False):
        profiles = UserProfile.objects.exclude(user=self.user).exclude(deactivated=True)

        # exclude those people that I am following
        following_people = [follow.target_userprofile.pk for follow in
                            Follow.objects.filter(user=self.user).exclude(is_blocked=True)]

        #profiles = profiles.exclude(pk__in=following_people)

        similar_users = []
        if not group_by_category:
            my_interests = self.get_interests()
            for profile in profiles:
                others_interests = profile.get_interests()
                # same_interests = my_interests.intersection(others_interests)
                # if same_interests:
                #     profile.similar_interests = Interest.objects.filter(id__in=same_interests)
                #     similar_users.append(profile)

            return similar_users
        else:
            my_interests = set([i.id for i in self.fitness_nutrition_interests.all()])
            similar_nutritions = []
            for profile in profiles:
                others_interests = set([i.id for i in profile.fitness_nutrition_interests.all()])
                # same_interests = my_interests.intersection(others_interests)
                # if same_interests:
                #     profile.similar_interests = Interest.objects.filter(id__in=same_interests)
                #     similar_nutritions.append(profile)

            my_interests = set([i.id for i in self.game_time_interests.all()])
            similar_gametimes = []
            for profile in profiles:
                others_interests = set([i.id for i in profile.game_time_interests.all()])
                same_interests = my_interests.intersection(others_interests)
                # if same_interests:
                #     profile.similar_interests = Interest.objects.filter(id__in=same_interests)
                #     similar_gametimes.append(profile)

            my_interests = set([i.id for i in self.fan_zone_interests.all()])
            similar_fanzones = []
            for profile in profiles:
                others_interests = set([i.id for i in profile.fan_zone_interests.all()])
                same_interests = my_interests.intersection(others_interests)
                # if same_interests:
                #     profile.similar_interests = Interest.objects.filter(id__in=same_interests)
                #     similar_fanzones.append(profile)

            ret = {
                'fanzone': similar_fanzones,
                'gametime': similar_gametimes,
                'nutrition': similar_nutritions
            }

            return ret


    def get_stats(self):
        """
            last view time
            fan_zone
            game_time
            fitness_nutrition
        """
        stats = {}

        try:
            if self.stats and 'time_stamps' in self.stats:
                time_stamps = self.stats.get('time_stamps')
                for feed in ('fan_zone', 'game_time', 'fitness_nutrition'):
                    stats[feed] = Post.objects.filter(feed=feed, created__gt=time_stamps.get(feed, '')).count()
        except:
            pass

        stats.update({
            'member_in_days': (datetime.date.today() - self.user.date_joined.date()).days,
            'hosted_event_count': self.events.count(),
            'joined_event_count': self.joined_events.count()
        })

        return stats

    def update_stats(self, feed):
        if not self.stats:
            self.stats = {}

        if 'time_stamps' not in self.stats:
            self.stats['time_stamps'] = {}

        self.stats['time_stamps'].update({feed: datetime.datetime.now()})
        self.save()

    def join_event(self, event_id):
        EventJoin.objects.create(event=Event.objects.get(id=event_id), profile=self)

    @property
    def get_son(self):
        return Child.objects.filter(gender='male').count()

    @property
    def get_daughter(self):
        return Child.objects.filter(gender='female').count()

utils.register(UserProfile)

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

class Child(models.Model):
    parent = models.ForeignKey(UserProfile, related_name='parent')
    avatar = models.ImageField(blank=True, null=True, upload_to='uploads/avatars', verbose_name="Child's Image")
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(choices=GENDER, max_length=10, verbose_name="I am", blank=True, null=True)
    interest = models.ManyToManyField(InterestCategory, null=True, blank=True)
    birthday = models.DateField(blank=True, null=True, help_text="Birthday")
    bio = models.TextField(blank=True, verbose_name="His/Her 's introduce")
    grade = models.PositiveSmallIntegerField(null=True, blank=True)

    def __unicode__(self):
        return self.full_name

    class Meta:
        verbose_name_plural = "Childs"

    def _get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)
    full_name = property(_get_full_name)

    def _get_parent_name(self):
        return '%s %s' % (self.parent.first_name, self.parent.last_name)
    parent_name = property(_get_parent_name)

    def get_age(self):
        from datetime import date
        if not self.birthday:
            return 0

        today = date.today()

        try:
            birthday = self.birthday.replace(year=today.year)
        except ValueError: # raised when birth date is February 29 and the current year is not a leap year
            birthday = self.birthday.replace(year=today.year, day=born.day-1)
        if birthday > today:
            return today.year - self.birthday.year - 1
        else:
            return today.year - self.birthday.year

class EventJoin(models.Model):
    profile = models.ForeignKey(UserProfile)
    event = models.ForeignKey(Event)
    created = models.DateTimeField(auto_now=True, auto_now_add=True)

class FacebookSessionError(Exception):
    def __init__(self, error_type, message, *args, **kwargs):
        super(FacebookSessionError, self).__init__(*args, **kwargs)
        self.message = message
        self.type = error_type

    def get_message(self):
        return self.message

    def get_type(self):
        return self.type

    def __unicode__(self):
        return u'%s: "%s"' % (self.type, self.message)


class FacebookSession(models.Model):
    access_token = models.CharField(max_length=103, unique=True)
    expires = models.IntegerField(null=True)

    user = models.ForeignKey(User, null=True)
    uid = models.BigIntegerField(unique=True, null=True)

    class Meta:
        unique_together = (('user', 'uid'), ('access_token', 'expires'))

    def query(self, object_id, connection_type=None, metadata=False):
        import urllib
        import simplejson

        url = 'https://graph.facebook.com/%s' % (object_id)
        if connection_type:
            url += '/%s' % (connection_type)

        params = {'access_token': self.access_token}
        if metadata:
            params['metadata'] = 1

        url += '?' + urllib.urlencode(params)
        response = simplejson.load(urllib.urlopen(url))
        if 'error' in response:
            error = response['error']
            raise FacebookSessionError(error['type'], error['message'])
        return response


def get_facebook_for_user(user):
    try:
        return FacebookSession.objects.get(user=user)
    except FacebookSession.DoesNotExist:
        return None


User.facebook = property(lambda u: get_facebook_for_user(u))
AnonymousUser.facebook = property(lambda u: None)


# Sets the User username field maxlength to 75
def longer_username(sender, *args, **kwargs):
    if sender.__name__ == "User" and sender.__module__ == "django.contrib.auth.models":
        sender._meta.get_field("username").max_length = 75


class_prepared.connect(longer_username)


class MailingAddress(models.Model):
    user = models.ForeignKey(User)
    address = models.CharField(max_length=200)
    address_2 = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=10)

    def __unicode__(self):
        return "%s %s, %s %s %s" % (self.address, self.address_2, self.city, self.state, self.zip)


CATEGORIES = (('fan_zone', "Fan Zone"),
              ('game_time', "Game Time"),
              ('fitness_nutrition', "Fitness and Nutrition"))

from social_auth.backends.facebook import FacebookBackend
from social_auth.backends import google
from social_auth.backends.twitter import TwitterBackend
from social_auth.signals import pre_update


def get_user_avatar(backend, details, response, social_user, uid, \
                    user, *args, **kwargs):
    if "id" in response:
        from urllib2 import urlopen, HTTPError
        from django.template.defaultfilters import slugify
        from django.core.files.base import ContentFile

        try:
            url = None
            if backend.__class__ == FacebookBackend:
                url = "http://graph.facebook.com/%s/picture?type=large" % response['id']

            elif backend.__class__ == TwitterBackend:
                url = response.get('profile_image_url', '').replace('_normal', '')

            if url:
                avatar = urlopen(url)

                try:
                    profile = user.profile
                except UserProfile.DoesNotExist:
                    import pdb;

                    pdb.set_trace()

                if 'gender' in response:
                    profile.gender = response.get('gender')

                if not profile.city:
                    profile.city = response.get('location') and response.get('location').get('name')

                if not profile.avatar and not profile.use_gravatar:
                    profile.avatar.save(slugify(user.username + " social") + '.jpg',
                                        ContentFile(avatar.read()))

                profile.save()

        except HTTPError:
            pass


