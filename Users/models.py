from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from Addresses.models import *

class LanguageCode(models.Model):
    name = models.CharField(max_length=16, null=False,blank=False,default='',verbose_name='Имя')
    code = models.CharField(max_length=5, null=False, blank=False, verbose_name='Код языка')

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = 'Код языка'
        verbose_name_plural = 'Коды языков'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.ForeignKey(Place, null=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/',default='')
    is_clinic = models.BooleanField(default=False)
    is_owner = models.BooleanField(default=False)
    languagecode = models.ForeignKey(LanguageCode,default='0')

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


