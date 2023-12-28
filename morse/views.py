from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from hashlib import sha256
from .models import MorseAudioPath
from django.contrib import messages
from django.contrib.messages import constants
from django.core.serializers import serialize
import json
from django.core.mail import send_mail, EmailMultiAlternatives
from .utils.decode_text import TextDecoder


def homepage(request):
    return render(request, 'homepage.html')


def decrypt_text_code(request):
    value_text = request.POST.get('text_code')
    decode = TextDecoder().start_lists_coders(value_text)


    return JsonResponse({'text_tranlated': decode})