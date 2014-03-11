# Create your views here.

import feedparser
from famdates.common.utils import json_view
from django.http import HttpResponse
import json
from django.core.serializers.json import DjangoJSONEncoder

#@json_view
def feed(request, name):
    d = feedparser.parse('http://www.scorespro.com/rss/live-soccer.xml')
    entries = [{'title': e.title, 'datetime': str(e.published)} for e in d.entries]
    return HttpResponse(json.dumps(entries, cls=DjangoJSONEncoder), 'application/json')