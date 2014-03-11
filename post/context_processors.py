from famdates.post.models import Post, Comment
from django.db.models import Q


def count(request):
    ret = {
        'fan_zone_feed_count': Post.objects.filter(feed='fan_zone').count(),
        'game_time_feed_count': Post.objects.filter(feed='game_time').count(),
        'fitness_nutrition_feed_count': Post.objects.filter(feed='fitness_nutrition').count(),
    }

    try:
        ret['comments_count'] = Comment.objects.filter(
            Q(post__author=request.user) | Q(post__wall=request.user)).count()
    except:
        pass

    return ret
        
