from django.db import models
from tinymce.models import HTMLField


class FAQS(models.Model):
    question = models.TextField(unique=True)
    answer = HTMLField()
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name_plural = 'Frequently Asked Questions'
        verbose_name = 'Frequently Asked Question'
