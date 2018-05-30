# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.conf import settings
import os
from django.http import JsonResponse
from .models import User, Brick, Photo


# Create your views here.
# session info: userID is id of logged in user, thisUser is username of logged in user

    # print ('-'*20)
    # print (request.session['sessionUserID'])
    # print (request.session['sessionUserName'])
    # print ('-'*20)


def index(request):
    # Message.objects.all().delete()
    context = {
        # 'sessionUser':User.objects.get(id=userID),
        'users':User.objects.all(),
        'dashboard':'active',
    }

    return render(request, 'social_media/index.html', context)


def account(request, id):
    print(id)

    context = {
        'sessionUser':User.objects.get(id=id),
        'users':User.objects.all(),
        'account':'active',
    }

    return render(request, 'social_media/account.html', context)


def new_message(request):
    if request.method == "POST":
        print (request.POST)
        # verify = Message.messageManager.create(request.POST)
        #
        # if verify == True:
        #     print ('success!')
        #     return redirect(reverse('social_media:index'))
        # else:
        #     print ('something went wrong')
        #     return redirect(reverse('social_media:index'))



def add_photo(request):

    context = {
        'photo':'active',
        'photos':Photo.objects.all()
    }
    if request.method == "POST":
        print ('gonna post')
        print (request.POST['filename'])

        # verify = Photo.photoManager.create(request.POST)
        #
        # if verify[0] == False:
        #     messages.add_message(request, messages.INFO, alert)
        #     return redirect(reverse('login_reg:add_photo'))
        #
        # elif verify[0] == True:
        #     pID = verify[1]
        #     thisPhoto = Photo.objects.get(id=pID)
        #     request.session['sessionPhoto'] = thisPhoto
        #     return redirect(reverse('social_media:add_photo'))
        # user = request.POST['user_id']
        # save_path = os.path.join(settings.MEDIA_ROOT, 'photos', request.FILES['img_file'])
        # path = default_storage.save(save_path, request.FILES['img_file'])
        id = request.POST['user_id']
        user = User.objects.get(id=id)

        instance = Photo.objects.create(user=user, filename=request.POST['filename'])
        return redirect(reverse('social_media:add_photo'))


    elif request.method == "GET":
        return render(request, 'social_media/add_photo.html', context)



def poop(request):
    context = {
        'account':'active',
        'users':User.objects.all(),
    }
    return render(request, 'social_media/account.html', context)
