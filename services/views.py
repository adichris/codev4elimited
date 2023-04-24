from .models import Service, ServicesContent
from django.views.generic import ListView, DetailView


class ServiceTemplateViews(ListView):
    template_name = 'services/list.html'
    model = Service

    def get_search(self):
        return self.request.GET.get('qservices')

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx['qvalue'] = self.get_search()
        ctx['title'] = 'Services'
        return ctx

    def get_queryset(self):
        searched = self.get_search()
        if searched:
            return self.model.objects.search(searched)
        else:
            return super().get_queryset()


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'services/detail.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = str(self.object)
        ctx['contents'] = ServicesContent.objects.filter(service=self.object)
        return ctx

