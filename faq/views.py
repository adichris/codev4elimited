from .models import FAQS
from django.views.generic import ListView


class FAQsListView(ListView):
    model = FAQS
    template_name = 'faqs/list.html'

    def get_context_data(self, *args, **kwargs):
        ctx = super().get_context_data(*args, **kwargs)
        ctx['title'] = 'Frequently Asked Questions'
        return ctx
