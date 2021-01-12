from django.shortcuts import render
from .models import *



def index(request):
    samples = Sample.objects.all()
    return render(request,'main/index.html', context={'samples':samples})

def fat(request):
    fats = Fat.objects.all()
    return render(request, 'main/fat.html', context={'fats':fats})

def sample_detail(request, slug):
    sample = Sample.objects.get(slug__iexact=slug)
    return render(request, 'main/sample_detail.html', context={'sample':sample})