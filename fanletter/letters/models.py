from django.db import models

class Song(models.Model):
    song_title = models.CharField(max_length=50)
    lyricist = models.CharField(max_length=10)
    composer = models.CharField(max_length=10)
    album_title = models.CharField(max_length=30)
    lyrics = models.TextField()

    def __str__(self):
        return self.song_title

class Letter(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE, null=True, blank=True)
    lyric_love_line = models.CharField(max_length=2, null=True, blank=True)
    letter_title = models.CharField(max_length=100)
    letter_abstract = models.CharField(max_length=128, null=True, blank=True)
    letter_content = models.TextField()
    today_rating = models.IntegerField(default=0)
    is_like = models.BooleanField(default=False)
    is_open = models.BooleanField(default=False)
    write_date = models.DateTimeField()

    def __str__(self):
        return  self.letter_title








