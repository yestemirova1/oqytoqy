from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from .entity import Entity


class Profile(Entity):
    user = models.OneToOneField(
        to=get_user_model(), verbose_name=_('user'), help_text=_('user'),
        on_delete=models.CASCADE, related_name='profile',
    )

    class Meta:
        db_table = 'common.profiles'
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    Profile.objects.create(user=instance) if created else None
