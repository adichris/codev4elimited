"""
URL configuration for codev4elimited project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from .main_urls import main_urlpatterns


handler404 = 'account.views.handler404'
handler500 = 'account.views.handler500'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(main_urlpatterns)),
    path('tinymce/', include('tinymce.urls')),
    path('services/', include('services.urls')),
    path('gallery/', include('gallery.urls')),
    path('faqs/', include('faq.urls')),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
