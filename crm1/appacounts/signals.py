from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import custumer

def custumer_profile(sender, instance, created,**kwargs):
    if created:
        group = Group.objects.get(name='custumer')
        instance.groups.add(group)

        custumer.objects.create(user = instance,
                                 name = instance.username)


post_save.connect(custumer_profile, sender=User)
