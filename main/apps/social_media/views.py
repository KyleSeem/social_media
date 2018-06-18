# -*- coding: utf-8 -*-
# apps/social_media/views.py

from __future__ import unicode_literals
import os

from PIL import Image
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.conf import settings
from django.http import JsonResponse
from .models import User, Photo, Post, Comment
from .forms import PhotoUploadForm, NewPostForm


# session info: userID is id of logged in user, thisUser is username of logged in user


###### NAVIGATION ######

# dashboard/main page
def index(request):
    # Photo.objects.all().delete()
    # request.session['pID'] = 8
    context = {
        'users':User.objects.all(),
        'posts':Post.objects.all().order_by('-created_at'),
        'photos':Photo.objects.all(),
        'nav_dashboard':'active',
        'launch':0
    }
    if 'pID' in request.session:
        if request.session['pID'] >= 1:
            context['new_pic'] = Photo.objects.get(id=request.session['pID'])

    if 'this_post' in request.session:
        context['this_post'] = Post.objects.get(id=request.session['this_post'])
        context['launch'] = 1


    return render(request, 'social_media/index.html', context)

# user's album
def myAlbum(request):
    context = {
        'myPhotos':Photo.objects.filter(user=request.session['sessionUserID']),
        'nav_myAlbum':'active'
    }
    if request.method == "GET":
        print ('-'*20)
        return render(request, 'social_media/album.html', context)



# user's acount page
def myAccount(request, **kwargs):
    ##### add validation to show only user's info OR change to id kwarg

    context = {
        'users':User.objects.all(),
        'nav_account':'active',
    }
    return render(request, 'social_media/account.html', context)



def view_post(request):
    if request.method == "POST":
        print ('-'*40)
        print request.POST['this_post']
        request.session['this_post'] = request.POST['this_post']


        return redirect(reverse('social_media:index'))
    # return render(request, 'social_media/index.html', context)


###### CRUD ######

# create photo - from image upload, validate and save
def add_photo(request):
    ####### use alerts array or messages????
    # alerts = []
    if request.method == "POST":
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            im = Image.open(request.FILES['photo'])
            if im.size[0] >= im.size[1]:
                orientation = 'ls'
            else:
                orientation = 'pt'

            new_photo = form.save()

            new_photo.orientation = orientation
            new_photo.save()

            request.session['pID'] = new_photo.id
            return redirect(reverse('social_media:index'))

        else:
            print ('invalid entry')
            return redirect(reverse('social_media:index'))


# delete photo - if user 'cancels' out of modal instead of submitting new post, delete the canceled photo from database
def scrap(request):
    if request.method == "POST":
        photo = Photo.objects.get(id=request.session['pID'])
        photo.delete()
        request.session['pID'] = 0
        return redirect(reverse('social_media:index'))


# create new post - takes image that was just saved and combines with user input
def new_post(request):
    if request.method == "POST":
        form = NewPostForm(request.POST)
        if form.is_valid():
            print ('valid post')
            post = form.save()
            request.session['pID'] = 0
            return redirect(reverse('social_media:index'))
        else:
            print ('invalid post')
            print form.errors
            return redirect(reverse('social_media:index'))
