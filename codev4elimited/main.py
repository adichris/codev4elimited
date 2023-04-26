from django.views.generic import TemplateView, CreateView
from services.models import Service
from account.models import ContactUs
from django.shortcuts import reverse
from account.forms import ContactUsCreationForm


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


class ContactUsPage(CreateView):
    template_name = 'home/contactus.html'
    model = ContactUs
    form_class = ContactUsCreationForm

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = 'Contact Us'
        has_contact = self.request.session.get('has_contact')
        if has_contact:
            del self.request.session['has_contact']
        ctx['has_contacted'] = has_contact
        return ctx

    def get_success_url(self):
        return reverse('contactus')

    def form_valid(self, form):
        self.request.session['has_contact'] = True
        return super().form_valid(form)
