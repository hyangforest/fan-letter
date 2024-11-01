import random
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

def unlucky_list(request):
    unluckys = Letter.objects.filter(song_id=1)
    lucky_50 = unluckys.filter(today_rating=2)  # 상
    lucky_30 = unluckys.filter(today_rating=1)  # 중
    lucky_00 = unluckys.filter(today_rating=0)  # 하

    first = random.choice(lucky_50) if lucky_50 else None
    second = random.choice(lucky_30) if lucky_30 else None
    third = random.choice(lucky_00) if lucky_00 else None

    letters = [
        {
            "battery": "5",
            "line": first.lyric_love_line,
            "title": first.letter_title,
            "abstract": first.letter_abstract,
            "like": first.is_like,
            "date": first.write_date.strftime("%d/%m/%Y %H:%M:%S")
        },
        {
            "battery": "3",
            "line": second.lyric_love_line,
            "title": second.letter_title,
            "abstract": second.letter_abstract,
            "like": second.is_like,
            "date": second.write_date.strftime("%d/%m/%Y %H:%M:%S")
        },
        {
            "battery": "0",
            "line": third.lyric_love_line,
            "title": third.letter_title,
            "abstract": third.letter_abstract,
            "like": third.is_like,
            "date": third.write_date.strftime("%d/%m/%Y %H:%M:%S")
        }
    ]

    return render(request, "letters/unlucky.html", {"letters": letters})

def unlucky_view(request, pk):
    # if pk == 1:
    #     return redirect("unlucky_list")
    # else:
    return render(request, "letters/unlucky-view.html")