from django.views.generic import ListView
from .models import Gallery


class GalleryListView(ListView):
    # template_name = 'gallery/list.html'
    template_name = 'gallery/animatedImagesList.html'
    model = Gallery

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx['title'] = 'Gallery'
        return ctx
