from django.urls import path

from . import views

urlpatterns = [
    path("account/<account_id>/card/<card_id>/launch", views.LaunchView.as_view()),
]
