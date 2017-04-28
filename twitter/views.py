
 # -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import AnonymousUser, User
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from datetime import datetime, timedelta
from django.utils import timezone
# Create your views here.
from .models import Tweet


def hello_world(request):
   return HttpResponse('HOLA <b style="color: red">MUNDO</b>')

def tweetear(request):
   if request.method == 'POST':
      u = User.objects.get(pk=request.user.id)
      texto = request.POST['texto']
      new_tweet = Tweet(message=texto, user=u)
      new_tweet.save()
      return redirect('index')
   return HttpResponse('HOLA <b style="color: red">SOLO PODES ACCEDER POR POST</b>')


def tweets(request):
    print request.user
    try:
        mis_tweets = Tweet.objects.order_by('-datetime')
    except:
        mis_tweets = None
    return render(request,
                  'tweets.html',
                  {'todos_los_tweets':mis_tweets})
    

def perfil(request):
    print request.user
    try:
        mis_tweets = Tweet.objects.filter(user=request.user).order_by('-datetime')
    except:
        mis_tweets = None
    return render(request,
                  'perfil.html',
                  {'todos_los_tweets':mis_tweets})
