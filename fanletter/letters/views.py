from django.shortcuts import render
from .models import Letter, Song

def letter_list(request):
    letters = Letter.objects.filter(is_open=True).select_related("song")

    return render(request,"letters/list.html" , {'letters': letters})

def letter_view(request, pk):
    if pk == 5:
        return letter_5(request)
    else:
        return render(request, "letters/letter.html")

def letter_5(request):
    return render(request, "letters/unlucky.html")