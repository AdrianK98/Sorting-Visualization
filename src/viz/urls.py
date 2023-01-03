from django.urls import path

from . import views

urlpatterns = [
    path("", views.bubble_sort, name="test"),
]
