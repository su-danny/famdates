from fileupload.models import MediaFile
from django.views.generic import CreateView, DeleteView

from django.http import HttpResponse, HttpResponseRedirect
from django.utils import simplejson
from django.core.urlresolvers import reverse

from django.conf import settings


def response_mimetype(request):
    if "application/json" in request.META['HTTP_ACCEPT']:
        return "application/json"
    else:
        return "text/plain"


class MediaFileCreateView(CreateView):
    model = MediaFile

    def form_invalid(self, form):
        return super(MediaFileCreateView, self).form_invalid(form)

    def form_valid(self, form):
        self.object = form.save()
        f = self.request.FILES.get('image') or self.request.FILES.get('video')

        if self.object.image:
            thumb = settings.MEDIA_URL + "file/" + f.name.replace(" ", "_")
        elif self.object.video:
            thumb = settings.STATIC_URL + "images/video_thumb.png"

        data = [{'name': f.name, 'url': settings.MEDIA_URL + "file/" + f.name.replace(" ", "_"),
                 'pk': self.object.pk,
                 'thumbnail_url': thumb,
                 'delete_url': reverse('upload-delete', args=[self.object.id]), 'delete_type': "DELETE"}]

        response = JSONResponse(data, {}, response_mimetype(self.request))
        response['Content-Disposition'] = 'inline; filename=files.json'
        return response

    def get_context_data(self, **kwargs):
        context = super(MediaFileCreateView, self).get_context_data(**kwargs)
        context['pictures'] = MediaFile.objects.all()
        return context


class MediaFileDeleteView(DeleteView):
    model = MediaFile

    def delete(self, request, *args, **kwargs):
        """
        This does not actually delete the file, only the database record.  But
        that is easy to implement.
        """
        self.object = self.get_object()
        self.object.delete()
        if request.is_ajax():
            response = JSONResponse(True, {}, response_mimetype(self.request))
            response['Content-Disposition'] = 'inline; filename=files.json'
            return response
        else:
            return HttpResponseRedirect('/upload/new')


class JSONResponse(HttpResponse):
    """JSON response class."""

    def __init__(self, obj='', json_opts={}, mimetype="application/json", *args, **kwargs):
        content = simplejson.dumps(obj, **json_opts)
        super(JSONResponse, self).__init__(content, mimetype, *args, **kwargs)
