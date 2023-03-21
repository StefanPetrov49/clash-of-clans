from django.db import models

from django.conf import settings as django_settings

# Create your models here.
class TownhallSelection(models.Model):
    text = models.CharField(
        max_length=20,
        blank=False,
        null=False,
    )
    thumbnail = models.ImageField(
        upload_to='townhall/'
    )

    def __str__(self):
        return self.text
