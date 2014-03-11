from static_page.views import static_page
from django.http import Http404
from django.conf import settings
from django.shortcuts import redirect
from social_auth.exceptions import AuthCanceled
from social_auth.middleware import SocialAuthExceptionMiddleware


class RegistrationMiddleware(object):
    def process_response(self, request, response):
        try:
            if response.status_code != 404 and request.user.is_authenticated():
                try:
                    profile = request.user.get_profile()
                    full_path = request.get_full_path()
                    if profile.current_registration_step and full_path != '/' and\
                            not full_path.startswith('/account/signup') and\
                            not full_path.startswith('/registration/update_interests') and\
                            not full_path.startswith('/registration/recommend_similar_users') and\
                            not full_path.startswith('/follow/toggle') and\
                            not full_path.startswith('/ajax-upload') and\
                            not full_path.startswith('/media/'):\
                        return redirect('/')

                    if profile.deactivated and not request.path_info.startswith('/account/deactivate/'):
                        return redirect('/account/deactivate/')

                except:
                    urls = set([u'/account/profile', '/account/home', u'/post', '/fan-zone', '/game-time',
                                '/fitness-nutrition'])
                    if any([request.path_info.startswith(url) for url in urls]):
                        return redirect('/registration/')
        except:
            pass

        return response


class SocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
    def raise_exception(self, request, exception):
        return False

    def get_message(self, request, exception):
        if isinstance(exception, AuthCanceled):
            return 'AuthCanceled!'
        return super(SocialAuthExceptionMiddleware, self) \
            .get_message(request, exception)

    def get_redirect_uri(self, request, exception):
        if request.user.is_authenticated():
            if isinstance(exception, AuthCanceled):
                return "/"

        return super(SocialAuthExceptionMiddleware, self).get_redirect_uri(request, exception)
