from django.core.management.base import BaseCommand, CommandError
from post.models import Post


class Command(BaseCommand):
    args = '...'
    help = 'help text ...'

    def handle(self, *args, **options):
        for video_post in Post.objects.filter(video__isnull=False, youtube_id__isnull=True):
            if video_post.video:
                print video_post, video_post.video
            