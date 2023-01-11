from django.urls import path

from . import views

urlpatterns = [
    path("card/<card_id>/launch/",
         views.LaunchView.as_view()),
]
