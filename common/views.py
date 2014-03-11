#import json
#from apps.common.models import City, Country
#from django.http import HttpResponse
#from apps.space.models import Lot
#
#def get_cities(request):
#    name = request.GET.get('name', '').lower()
#    ret = ['Marina, San Francisco, CA', 'Mission District, San Francisco, CA', 'Civic Center, San Francisco' ]
#
#    try:
#        if None: # Not use cities any more
#            country = Country.objects.using('city').get(code = 'USA')
#            cities = City.objects.using('city').filter(countrycode=country)
#            if name:
#                cities = cities.filter(name__istartswith=name)[:15]
#            ret = [city.name for city in cities]
#    except:
#        pass
#    ret = [l for l in ret if name in l.lower()]
#    ret = [l.name for l in Lot.objects.filter(name__icontains=name)[:10]] + ret
#    
#    return HttpResponse(json.dumps(ret), mimetype='application/json')