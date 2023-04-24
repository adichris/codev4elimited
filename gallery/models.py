from django.db import models
from django.utils.text import slugify
import os


def upload_gallery_image(instance, filename):
    return os.path.join('gallery', instance.title, 'image', filename)


class Gallery(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=120, null=True, blank=True)
    