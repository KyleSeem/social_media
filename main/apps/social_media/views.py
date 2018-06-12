# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.conf import settings
from django.http import JsonResponse
from .models import User, Brick, Photo, Comment


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
        'photos':Photo.objects.all(), # change this to bricks
        'nav_dashboard':'active_page',
        # 'nav_dashboard':'active',
    }

    return render(request, 'social_media/index.html', context)


def account(request, id):
    print(id)

    context = {
        'sessionUser':User.objects.get(id=id),
        'users':User.objects.all(),
        'nav_account':'active_page',
        # 'nav_account':'active',
    }

    return render(request, 'social_media/account.html', context)


def new_brick(request, id):
    context = {
        'pic':Photo.objects.get(id=id)
    }
    if request.method == "GET":
        return render(request, 'social_media/new_brick.html', context)

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
        'nav_photo':'active_page',
        # 'nav_photo':'active',
        'photos':Photo.objects.all()
    }
    if request.method == "GET":
        return render(request, 'social_media/add_photo.html', context)

    elif request.method == "POST":
        # set validation
        id = request.POST['user']
        new_photo = Photo()
        new_photo.user = User.objects.get(id=id)
        new_photo.photo = request.FILES['photo']
        new_photo.save()
        saved = True

        picID = new_photo.id
        return redirect(reverse('social_media:new_brick', kwargs={'id':picID}))



def myAlbum(request):
    context = {
        'myPhotos':Photo.objects.filter(user=request.session['sessionUserID']),
        'nav_myAlbum':'active_page'
        # 'nav_myAlbum':'active'
    }
    if request.method == "GET":
        print ('-'*20)
        return render(request, 'social_media/album.html', context)





def poop(request):
    context = {
        'nav_account':'active',
        'users':User.objects.all(),
    }
    return render(request, 'social_media/account.html', context)
