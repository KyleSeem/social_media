# -*- coding: utf-8 -*-
# apps/social_media/views.py

from __future__ import unicode_literals
import os

from PIL import Image, ExifTags
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.conf import settings
from django.http import JsonResponse
from .models import User, Photo, Brick, Comment
from .forms import PhotoUploadForm


# Create your views here.
# session info: userID is id of logged in user, thisUser is username of logged in user

    # print ('-'*20)
    # print (request.session['sessionUserID'])
    # print (request.session['sessionUserName'])
    # print ('-'*20)

# dashboard/main page
def index(request):
    # Photo.objects.all().delete()
    # request.session['pID'] = 0
    context = {
        'users':User.objects.all(),
        'photos':Photo.objects.all(), # change this to bricks
        'nav_dashboard':'active',
    }
    if 'pID' in request.session:
        if request.session['pID'] >= 1:
            context['new_pic'] = Photo.objects.get(id=request.session['pID'])
    return render(request, 'social_media/index.html', context)


# user's acount page
def myAccount(request):
    ##### add validation to show only user's info OR change to id kwarg
    context = {
        # 'sessionUser':User.objects.get(id=id),
        'users':User.objects.all(),
        'nav_account':'active',
    }
    return render(request, 'social_media/account.html', context)


def new_post(request):
    # take photo that was just saved, load page as if it were the dash, but include the id of the new pic, trigger modal pop with form for new post
    if request.method == "POST":
        print (request.POST)
        request.session['pID'] = 0
        return redirect(reverse('social_media:index'))
        # verify = Message.messageManager.create(request.POST)
        #
        # if verify == True:
        #     print ('success!')
        #     return redirect(reverse('social_media:index'))
        # else:
        #     print ('something went wrong')
        #     return redirect(reverse('social_media:index'))

# if user 'cancels' out of modal instead of submitting new brick, delete the canceled photo from database
def scrap(request):
    request.session['pID'] = 0
    if request.method == "POST":
        print request.POST
        print request.session['pID']
        return redirect(reverse('social_media:index'))


def add_photo(request):
    if request.method == "POST":
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            print ('valid entry')
            new_photo = form.save()
            request.session['pID'] = new_photo.id

            return redirect(reverse('social_media:index'))

        else:
            print ('invalid entry')
            return redirect(reverse('social_media:index'))




def myAlbum(request):
    context = {
        'myPhotos':Photo.objects.filter(user=request.session['sessionUserID']),
        'nav_myAlbum':'active'
    }
    if request.method == "GET":
        print ('-'*20)
        return render(request, 'social_media/album.html', context)
