from django.views.generic import TemplateView
from services.models import Service


class HomePage(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['services'] = Service.objects.get_featured()
        return ctx


class WhoWeArePage(TemplateView):
    template_name = 'home/whoweare.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = 'Who We Are'
        return ctx


class LocationPage(TemplateView):
    template_name = 'home/whoweare.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = 'Location'
        return ctx

