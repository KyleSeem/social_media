# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

from PIL import Image, ImageFile
import os
from django.db import models
from ..login_reg.models import User

def get_img_path(instance, filename):
    return os.path.join(settings.MEDIA_ROOT, 'photos', )


# Create your models here.
# class PhotoManager(models.Manager):
#
#     def create(self, postData):
#         if not postData:
#             alerts.append('Please select an image')
#             return (False, alerts)
#         else:
#             user_id = User.objects.get(id=postData['user_id'])
#             filename = str(postData['filename'])
#             instance = Photo.objects.create(user_id=user_id, filename=filename)
#             print ('-'*20)
#             print (instance.id, instance.user_id, instance.filename, instance.img_path)
#             return (True, instance.id)


class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    filename = models.CharField(max_length=55)
    img_path = models.ImageField(upload_to='media/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class BrickManager(models.Manager):
    def create(self, postData):
        if not postData:
            print ('no data')
            return False
        else:
            user_id = User.objects.get(id=postData['user_id'])
            message = postData['message']
            img_file = postData['img_file']

            print(user_id, message, img_file)

            brick = Brick.objects.create(user_id=user_id, message=message, img_file=img_file)
            print ('-'*20)
            print (brick.id, brick.user_id, brick.message, brick.img_file)
            return (True)





class Brick(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    img_file = models.ForeignKey(Photo, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    brickManager = BrickManager()
    objects = models.Manager()


class Comment(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    brick_id = models.ForeignKey(Brick, on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
