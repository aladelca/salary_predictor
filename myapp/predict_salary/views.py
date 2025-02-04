from django.shortcuts import render, redirect
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .models import JobPosting
# Create your views here.

def index(request):
    return render(request, 'index.html')

def upload(request):
    if request.method == 'POST' and request.FILES.get('document'):
        document = request.FILES['document']
        JobPosting.objects.create(document = document)
        return render(request, 'upload.html')
    return render(request, 'upload.html')
