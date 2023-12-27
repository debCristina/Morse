from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from hashlib import sha256
from .models import Usuario
from django.contrib import messages
from django.contrib.messages import constants
from django.core.serializers import serialize
import json
from django.core.mail import send_mail, EmailMultiAlternatives



def homepage(request):
    return render(request, 'homepage.html')


def user(request):
    usuario = 'thiago'
    return render(request, 'usuario.html', {'user': usuario})