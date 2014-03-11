from django.conf import settings
from django.core.paginator import Paginator, InvalidPage
from django.db.models import Q
from django.shortcuts import render_to_response, render
from django.template import RequestContext

from famdates.account.models import UserProfile, Interest
from famdates.post.models import Post
from django.contrib.auth.decorators import login_required
from famdates.group.models import Group


@login_required
def simple_search(request):
    qname = request.GET.get('name')
    q = request.GET.get('q')
    qinterest = request.GET.get('interest')
    qzip_code = request.GET.get('zip_code')

    template_name = 'search/results.html'

    profile_results = UserProfile.objects.all().exclude(deactivated=True)
    interest_results = Interest.objects.all()

    if not q:
        if qname:
            profile_results = profile_results.filter(
                Q(user__first_name__icontains=qname) | Q(user__last_name__icontains=qname))
            interest_results = interest_results.filter(name__icontains=qname)

        if qinterest:
            profile_results = profile_results.filter(
                Q(fan_zone_interests__name=qinterest) | Q(fitness_nutrition_interests__name=qinterest) | Q(
                    game_time_interests__name=qinterest))

            #    if qzip_code:
            #        profile_results = profile_results.filter(zipcode__icontains=qzip_code)
        post_results = None
        team_results = []
    else:
        interest_results = interest_results.filter(name__icontains=q)
        profile_results = profile_results.filter(Q(fan_zone_interests__name=q) |
                                                 Q(fitness_nutrition_interests__name=q) |
                                                 Q(game_time_interests__name=q) |
                                                 Q(user__first_name__icontains=q) | Q
                                                     (user__last_name__icontains=q) |
                                                 Q(state__icontains=q) |
                                                 Q(city__icontains=q)).distinct()
        post_results = Post.objects.filter(body__icontains=q).order_by('-created')
        team_results = Group.objects.filter(Q(name__icontains=q) |
                                            Q(owner__first_name__icontains=q) |
                                            Q(owner__last_name__icontains=q) |
                                            Q(about__icontains=q) |
                                            Q(city__icontains=q)).distinct()

    ctx = {
        'people_results': profile_results.filter(acct_type='individual'),
        'team_results': team_results,
        'interest_results': interest_results,
        'post_results': post_results,
    }

    return render(request, template_name, ctx)


import math


def distance(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371 # km

    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) \
                                                  * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(
        dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radius * c

    return d


@login_required
def similar_user_search(request):
    qname = request.GET.get('similar_users')

    _qname = qname.split()
    if _qname:
        firstName = _qname[0]
        if len(_qname) > 1:
            lastName = _qname[1]
        else:
            lastName = None
    else:
        lastName = firstName = None

    lastName = request.GET.get('lastName')
    q = request.GET.get('q')
    qinterests = request.GET.getlist('interests')

    qzip_code = request.GET.get('zip_code')
    qdistance = request.GET.get('distance')

    template_name = 'search/similar_user_results.html'

    profile = request.user.get_profile()

    similar_profiles = profile.get_similar_profiles()
    profile_results = similar_users = UserProfile.objects.other_profiles(request.user).filter(
        pk__in=[p.pk for p in similar_profiles])

    interest_results = Interest.objects.all()

    if not q:
        if firstName:
            profile_results = profile_results.filter(user__first_name__icontains=firstName)

        if lastName:
            profile_results = profile_results.filter(user__last_name__icontains=lastName)

        if qinterests:
            profile_results = profile_results.filter(
                Q(fan_zone_interests__pk__in=qinterests) | Q(fitness_nutrition_interests__pk__in=qinterests) |
                Q(game_time_interests__pk__in=qinterests)).values('id')

            # MySQL does not support distinct operation                                        
            profile_results = UserProfile.objects.filter(id__in=set([r['id'] for r in profile_results]))

        if qzip_code:
            profile_results = profile_results.filter(Q(city__icontains=qzip_code) | Q(zipcode__icontains=qzip_code))

        if qdistance:
            ranges = {'1': (0, 20),
                      '20': (20, 10000)}

            from zipdistance.models import ZipDistance

            try:
                target = ZipDistance.objects.get(zipcode=request.user.get_profile().zipcode or '94104')
                target = (target.latitude, target.longitude)

                zip_results = []

                if qdistance in ranges:
                    _from, _to = ranges[qdistance]
                    zips = ZipDistance.objects.filter(zipcode__in=[p.zipcode for p in profile_results if p.zipcode])
                    for zip in zips:
                        pos = (zip.latitude, zip.longitude)
                        d = distance(target, pos)
                        if d > _from and d < _to:
                            zip_results.append(zip.zipcode)

                    profile_results = profile_results.filter(zipcode__in=zip_results)

            except ZipDistance.DoesNotExist:
                """
                User did not have a valid zipcode
                """
                pass
            except:
                pass
    else:
        profile_results = profile_results.filter(Q(fan_zone_interests__name=q) |
                                                 Q(fitness_nutrition_interests__name=q) |
                                                 Q(game_time_interests__name=q) |
                                                 Q(user__first_name__icontains=q) | Q
                                                     (user__last_name__icontains=q) |
                                                 Q(state__icontains=q) |
                                                 Q(city__icontains=q)).distinct()

    _profile_results = {}
    for p in profile_results:
        _profile_results[p.id] = True

    ctx = {
        'similar_profiles': [u for u in similar_profiles if u.id in _profile_results],
        'similar_users': similar_users,
    }

    return render(request, template_name, ctx)
    
    

