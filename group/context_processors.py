from .models import UserGroup
from django.db.models import Q


def count(request):
    ret = {'group_count': 0}

    try:
        ret['group_count'] = UserGroup.objects.all().count()
    except:
        pass

    return ret
        
