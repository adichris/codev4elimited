from django.db import models
import os
from django.utils.text import slugify
from tinymce.models import HTMLField
from django.shortcuts import reverse


def flyer_upload_to(instance, filename):
    return os.path.join('services', instance.name, 'flyer', filename)


def services_content_image_upload_to(instance, filename):
    return os.path.join('services', instance.service.name, 'content', filename)


class ServiceManager(models.Manager):
    def get_featured(self):
        return self.filter(featured=True)

    def search(self, query):
        return self.filter(
            models.Q(headline__icontains=query) | models.Q(description__icontains=query)
        )


class Service(models.Model):
    flyer = models.ImageField(upload_to=flyer_upload_to)
    headline = models.TextField(unique=True)
    description = models.TextField(null=True, blank=True)
    slug = models.SlugField(blank=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=True)
    objects = ServiceManager()

    @property
    def name(self):
        return self.slug.replace('-', '')[:61]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.headline)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.headline

    def get_absolute_url(self):
        return reverse('Services:detail', kwargs={
            'slug': self.slug
        })


class ServicesContent(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to=services_content_image_upload_to)
    content = HTMLField(null=True, blank=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

