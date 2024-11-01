from django.urls import path

from . import views

app_name = "letters"
urlpatterns = [
    path("", views.letter_list, name="letter_list"),
    path("<int:pk>/", views.letter_view, name="letter_view"),
    path("unlucky/", views.unlucky_list, name="unlucky_list"),
    path("unlucky/<int:pk>/", views.unlucky_view, name="unlucky_view"),
]