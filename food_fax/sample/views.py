from django.shortcuts import render
from .models import Sample

def index(request):
    context = {
        'samples': Sample.objects.all()
    }
    return render(request, 'pages/demo.html', context)