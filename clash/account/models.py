from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

UserModel = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE
    )

    player_tag = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )
    icon = models.URLField(
        blank=True,
        null=True
    )
    trophies = models.IntegerField(
        blank=True,
        null=True
    )


@receiver(post_save, sender=UserModel)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=UserModel)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
