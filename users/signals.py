from django.db.models.signals import post_save, post_delete
from django.contrib.auth.models import User
from .models import Profile


def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )


def updateUser(sender, instance, created, **kwargs):
    profile = instance # got the updated data
    user = profile.user 
    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()

# def updateProfile(sender, instance, created, **kwargs):
#     user = instance
#     profile = Profile.objects.get(username = user.username) 
#     if created == False:
#         profile.name = user.first_name
#         profile.email = user.email        
#         profile.save()



post_save.connect(createProfile, sender=User)


post_save.connect(updateUser, sender=Profile)

# when User is changed this function will be triggered and 
# updates profile model accordingly
# post_save.connect(updateProfile, sender=User) 

post_delete.connect(deleteUser, sender=Profile)
