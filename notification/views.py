from django.contrib.auth.decorators import login_required
import json
from django.http import HttpResponseRedirect, HttpResponse, Http404
from notification.models import Notification


@login_required
def user_notifications(request):
    if request.user.email:
        ret = [{'title': notification.subject}\
                for notification in  Notification.objects.filter(recipients__icontains=request.user.email).order_by('-created')]
    else:
        ret = []

    return HttpResponse(json.dumps(ret))