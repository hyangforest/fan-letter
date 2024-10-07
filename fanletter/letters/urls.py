from django.urls import path

from . import views

app_name = "letters"
urlpatterns = [
    path("", views.letter_list, name="letter_list"),
    path("<int:pk>/", views.letter_view, name="letter_view"),
]