from django.urls import path
from .views import ServiceTemplateViews, ServiceDetailView


app_name = 'Services'
urlpatterns = [
    path('', ServiceTemplateViews.as_view(), name='list'),
    path('<slug:slug>/', ServiceDetailView.as_view(), name='detail'),
]

