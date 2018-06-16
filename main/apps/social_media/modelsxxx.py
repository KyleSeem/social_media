# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

from PIL import Image, ImageFile
import os
from django.db import models
from django.forms import ModelForm
from ..login_reg.models import User


# Create your models here.
def upload_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)

class BrickManager(models.Manager):
    def create(self, postData):
        if not postData:
            alerts.append('Please select an image')
            return (False, alerts)
        else:
            print ('true')
            return (True)





class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=upload_path)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'photos'


class Brick(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    caption = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    brickManager = BrickManager()
    objects = models.Manager()

    class Meta:
        db_table = 'bricks'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    brick = models.ForeignKey(Brick, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comments'
