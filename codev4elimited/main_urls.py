from django.urls import path
from .main import HomePage, WhoWeArePage


main_urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('whoweare/', WhoWeArePage.as_view(), name='whoweare'),
]


