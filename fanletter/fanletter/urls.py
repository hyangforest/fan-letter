from django.contrib import admin
from django.urls import path, include
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('letters/', include('letters.urls')),
    path('', index, name='index'),
]
