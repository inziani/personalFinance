from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from accounts.models import User, UserProfile

@receiver(post_save, sender=User)
def createUserProfile(sender, instance, created, **kwargs):
  if created:
    UserProfile.objects.create(user = instance)