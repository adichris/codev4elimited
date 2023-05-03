from django.views.generic import ListView, DetailView
from .models import Team
from django.shortcuts import get_object_or_404, render


class OurTeamTemplateView(ListView):
    # template_name = 'account/our-team.html'
    template_name = 'account/our-team-animate.html'
    model = Team

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = 'Our Team'
        return ctx


class TeamMemberDetailView(DetailView):
    template_name = 'account/team-detail.html'
    model = Team

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = str(self.object)
        return ctx

    def get_object(self, queryset=None):
        return get_object_or_404(
            self.model,
            profile__slug=self.kwargs['slug']
        )


def handler404(request, *args, **kwargs):
    return render(request, 'error/404.html', {
        'title': 'Page Not Found'
    })


def handler500(request, *args, **kwargs):
    return render(request, 'error/500.html', {
        'title': 'Server Error'
    })
