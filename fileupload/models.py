from django.db import models
from django.contrib.auth.models import User


class MediaFile(models.Model):
    image = models.FileField(upload_to="file", blank=True, null=True)
    video = models.FileField(upload_to="file", blank=True, null=True)
    content_type = models.CharField(max_length=50, default='image', blank=True)
    created_at = models.DateTimeField(auto_now=True, auto_now_add=True)
    user = models.ForeignKey(User, blank=True, null=True)

    def __unicode__(self):
        file = self.video or self.image
        if file: return file.name

        return ''

    @models.permalink
    def get_absolute_url(self):
        return ('upload-new', )

    def save(self, *args, **kwargs):
        super(MediaFile, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.image: self.image.delete(False)
        if self.video: self.video.delete(False)

        super(MediaFile, self).delete(*args, **kwargs)
