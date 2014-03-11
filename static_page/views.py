from static_page.models import *
from django.template import loader, RequestContext
from django.shortcuts import get_object_or_404
from django.http import Http404, HttpResponse, HttpResponsePermanentRedirect
from django.conf import settings
from django.core.xheaders import populate_xheaders
from django.utils.safestring import mark_safe
from django.views.decorators.csrf import csrf_protect

DEFAULT_TEMPLATE = 'static_page/default.html'

# This view is called from FlatpageFallbackMiddleware.process_response
# when a 404 is raised, which often means CsrfViewMiddleware.process_view
# has not been called even if CsrfViewMiddleware is installed. So we need
# to use @csrf_protect, in case the template needs {% csrf_token %}.
# However, we can't just wrap this view; if no matching flatpage exists,
# or a redirect is required for authentication, the 404 needs to be returned
# without any CSRF checks. Therefore, we only
# CSRF protect the internal implementation.
def static_page(request, url):
    """
    Public interface to the flat page view.

    Models: `flatpages.flatpages`
    Templates: Uses the template defined by the ``template_name`` field,
        or `flatpages/default.html` if template_name is not defined.
    Context:
        flatpage
            `flatpages.flatpages` object
    """
    if not url.startswith('/'):
        url = '/' + url
    try:
        f = get_object_or_404(StaticPage,
                              url__exact=url, sites__id__exact=settings.SITE_ID)
    except Http404:
        if not url.endswith('/') and settings.APPEND_SLASH:
            url += '/'
            f = get_object_or_404(StaticPage,
                                  url__exact=url, sites__id__exact=settings.SITE_ID)
            return HttpResponsePermanentRedirect('%s/' % request.path)
        else:
            raise
    return render_flatpage(request, f)


@csrf_protect
def render_flatpage(request, f):
    """
    Internal interface to the flat page view.
    """
    # If registration is required for accessing this page, and the user isn't
    # logged in, redirect to the login page.
    if f.registration_required and not request.user.is_authenticated():
        from django.contrib.auth.views import redirect_to_login

        return redirect_to_login(request.path)
    if f.template_name:
        t = loader.select_template((f.template_name, DEFAULT_TEMPLATE))
    else:
        t = loader.get_template(DEFAULT_TEMPLATE)

    # To avoid having to always use the "|safe" filter in flatpage templates,
    # mark the title and content as already safe (since they are raw HTML
    # content in the first place).
    try:
        current_language = request.LANGUAGE_CODE
    except:
        # request do not have LANGUAGE_CODE
        current_language = 'en-us'
    if current_language == 'en-us': current_language = 'en'

    p = f.contents.get(language=current_language)

    p.title = mark_safe(p.title)
    p.content = mark_safe(p.content)
    p.children = []
    for child in f.children.all():
        p.children.append(child)

    c = RequestContext(request, {
        'static_page': p,
    })
    response = HttpResponse(t.render(c))
    populate_xheaders(request, response, StaticPage, f.id)
    return response
