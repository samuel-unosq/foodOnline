from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import User, UserProfile


@receiver(post_save, sender=User) # new form decorator connect
def post_save_create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        print('User is created')
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            # create the user profile if not exist
            UserProfile.objects.create(User=instance)
            print('Profile doent exist, but I created one.')
        print('User is updated')
# post_save.connect(post_save_create_profile, User) # old way

@receiver(pre_save, sender=User)
def pre_save_profile_receiver(sender, instance, **kwargs):
    print(f'This user would be saved {instance.username}')
