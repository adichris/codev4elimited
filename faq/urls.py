from django.urls import path
from .views import FAQsListView


app_name = 'FAQs'
urlpatterns = [
    path('', FAQsListView.as_view(), name='list'),
]
