# coding: utf8
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from Addresses.models import Place
from phonenumber_field.modelfields import PhoneNumberField


class UserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(default='', max_length=64, null=False, blank=False, verbose_name='Имя')
    date_of_birth = models.DateField()
    location = models.ForeignKey(Place, default='',null=True, verbose_name='Место')
    is_active = models.BooleanField(default=True, verbose_name='Активный')
    is_admin = models.BooleanField(default=False, verbose_name='Админ')
    is_owner = models.BooleanField(default=False, verbose_name='Владелец')
    is_moder = models.BooleanField(default=False, verbose_name='Модератор')
    is_clinic = models.BooleanField(default=False, verbose_name='Клиника')
    phone_number = PhoneNumberField(default='', verbose_name='Контактный телефон')
    fax_number = PhoneNumberField(blank=True, verbose_name='Факс')
    avatar = models.ImageField(upload_to='avatars/',default='avatars/nopic.jpg')

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth']

    def image_tag(self):
        return u'<img width="100" src="/media/%s" />' % (self.avatar)

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        '''if self.first_name == '':
        //   return self.first_name + ' ' + self.second_name
        //else:'''
        return self.first_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        if self.is_admin or self.is_moder:
            return True
        else:
            return False

    @property
    def isowner(self):
        if self.is_owner:
            return True
        else:
            return False

    @property
    def isclinic(self):
        if self.is_clinic:
            return True
        else:
            return False
