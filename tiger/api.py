from tastypie.authentication import Authentication
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from tastypie.exceptions import ImmediateHttpResponse
from tastypie.http import HttpUnauthorized
from .models import Card


class DjangoLoggedInAuthentication(Authentication):
    def is_authenticated(self, request, **kwargs):
        if request.user.is_authenticated():
            return True
        return False


class CardResource(ModelResource):
    class Meta:
        queryset = Card.objects.all()
        resource_name = 'card'
        excludes = ['fingerprint', 'user', 'stripe_id']
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        authentication = DjangoLoggedInAuthentication()
        authorization = Authorization()

    def apply_authorization_limits(self, request, object_list):
        return object_list.filter(user=request.user)

    def is_authorized(self, request, object=None):
        super(CardResource, self).is_authorized(request, object)
        if object and (object.user != request.user):
            raise ImmediateHttpResponse(response=HttpUnauthorized())
            
    