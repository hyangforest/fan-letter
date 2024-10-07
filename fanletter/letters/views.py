from django.shortcuts import render
from .models import Letter

def letter_list(request):
    objects = Letter.objects.all()
    return render(request,"letters/index.html" , {'objects': objects})