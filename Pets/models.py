# coding: utf8
from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class PetType(models.Model):
    name = models.CharField(max_length=32, null=False, blank=False, verbose_name='Тип')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип животного'
        verbose_name_plural = 'Типы животных'

class PetBreed(models.Model):
    type = models.ForeignKey(PetType)
    name = models.CharField(max_length=32, null=False, blank=False, verbose_name='Порода')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Порода'
        verbose_name_plural = 'Породы'

class Petcolor(models.Model):
    name = models.CharField(max_length=16, blank=False, null=False, unique=True, verbose_name='Окрас')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Окрас'
        verbose_name_plural = 'Окрас'

class Pet(models.Model):
    name = models.CharField(max_length=32, blank=False, null=False, verbose_name='Кличка')
    chip_id = models.CharField(max_length=16, blank=False, null=False, verbose_name='ID чипа',unique=True)
    owner = models.ForeignKey(User,related_name='+', verbose_name='Хозяин')
    breed = models.ForeignKey(PetBreed,verbose_name='Порода')
    birthday = models.DateField(verbose_name='Дата рождения',null=True)
    registrator = models.ForeignKey(User,  related_name='+', verbose_name='Регистратор')
    registrationdate = models.DateField(auto_now_add=True, null=True, verbose_name='Дата регистрации')
    image = models.ImageField(upload_to='pets/',default='/pets/nopet.jpg', verbose_name='Аватар')
    special = models.TextField(blank=True, null=True, verbose_name='Особые приметы')

    def image_tag(self):
        return u'<img width="100" src="/media/%s" />' % (self.image)

    image_tag.short_description = 'Картинка'
    image_tag.allow_tags = True

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Животные'
        verbose_name = 'Животные'