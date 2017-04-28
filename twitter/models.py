from __future__ import unicode_literals
from django.conf import settings
from django.db import models

# Create your models here.
class Tweet(models.Model):
    message = models.CharField(max_length=142)
    datetime = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    puajs = models.ManyToManyField(settings.AUTH_USER_MODEL, 
                                    blank=True, 
                                    related_name='mis_puajs')
    def reguaus(self):
        return ReGuau.objects.filter(tweet=self).count()

    def count_puaj(self):
        return puajs.objects.count()

    def __str__(self):
        return 'Tweet nro {} - by {}'.format(self.id, self.user)

class ReGuau(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    tweet = models.ForeignKey(Tweet)
    comment = models.CharField(max_length=143)


# mkvirtualenv [mi_entorno]
# pip install django
# django-admin startproject twitter
# cd twitter
# django-admin startapp twitter_app