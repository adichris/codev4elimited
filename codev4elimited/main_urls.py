from django.urls import path
from .main import HomePage, WhoWeArePage, ContactUsPage
from account.views import OurTeamTemplateView, TeamMemberDetailView

main_urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('who-we-are/', WhoWeArePage.as_view(), name='whoweare'),
    path('contact-us/', ContactUsPage.as_view(), name='contactus'),
    path('our-team/', OurTeamTemplateView.as_view(), name='our-team'),
    path('our-team/<slug:slug>/', TeamMemberDetailView.as_view(), name='our-team-member'),
]
