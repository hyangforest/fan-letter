from django.shortcuts import render, redirect
from .models import Letter, Song

def letter_list(request):
    letters = Letter.objects.filter(is_open=True).select_related("song")

    return render(request,"letters/list.html" , {'letters': letters})

def letter_view(request, pk):
    if pk == 1:
        return redirect("letters:unlucky_list")
    else:
        return render(request, "letters/letter.html")

def letter_1(request):
    letter = Letter.objects.filter(id=1).first()

    return render(request, "letters/unlucky.html")

def unlucky_list(request):
    return render(request, "letters/unlucky.html")

def unlucky_view(request, pk):
    # if pk == 1:
    #     return redirect("unlucky_list")
    # else:
    return render(request, "letters/unlucky-view.html")