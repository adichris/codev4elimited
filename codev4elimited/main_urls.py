from django.urls import path
from .main import HomePage


main_urlpatterns = [
    path('', HomePage.as_view(), name='home'),
]

