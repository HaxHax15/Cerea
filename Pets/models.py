# coding: utf8
from django.db import models

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


class Pet(models.Model):
    name = models.CharField(max_length=32, blank=False, null=False, verbose_name='Кличка')
    chip_id = models.CharField(max_length=16, blank=False, null=False, verbose_name='ID чипа',unique=True)
    owner = models.ForeignKey('Users.User', limit_choices_to={'is_owner':True},related_name='+')
    breed = models.ForeignKey(PetBreed)
    registrator = models.ForeignKey('Users.User', limit_choices_to={'is_clinic':True}, related_name='+')
    image = models.ImageField(upload_to='pets/',default='/pets/nopet.jpg')

    def image_tag(self):
        return u'<img width="100" src="/media/%s" />' % (self.image)

    image_tag.short_description = 'Картинка'
    image_tag.allow_tags = True

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Животные'
        verbose_name = 'Животные'