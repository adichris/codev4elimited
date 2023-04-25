from django.urls import path
from .views import GalleryListView


app_name = 'Gallery'
urlpatterns = [
    path('', GalleryListView.as_view(), name='list')
]
