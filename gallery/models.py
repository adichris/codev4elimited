from django.db import models
from django.utils.text import slugify
import os


def upload_gallery_image(instance, filename):
    return os.path.join('gallery', instance.title, 'image', filename)


class Gallery(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=120, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    tag = models.CharField(null=True, blank=True, max_length=120)

    def save(self, *args, **kwargs):
        if self.title:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title or 'Gallery ' + str(self.id)
