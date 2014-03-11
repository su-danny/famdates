from account.models import Interest


def profile(request):
    profile = None
    if request.user.is_authenticated():
        try:
            profile = request.user.get_profile()
            return {'profile': profile,
                    'fanzone': Interest.objects.filter(category__name='fan_zone'),
                    'gametime': Interest.objects.filter(category__name='game_time'),
                    'nutrition': Interest.objects.filter(category__name='fitness_nutrition')}

        except:
            pass
    return {}
