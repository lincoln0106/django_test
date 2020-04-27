# models.py
# from __future__ import unicode_literals
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
class Student(models.Model):
    name = models.CharField(max_length= 100, verbose_name= '名称')
    sex =  models.CharField(max_length= 20, verbose_name= '性别')
    sid = models.CharField( max_length=100, default='0',verbose_name='sid')


    def __unicode__(self):
        return '%d: %s' % (self.pk, self.name)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)