from django.contrib import admin
from .models import Letter, Song

admin.site.register([Letter, Song])

