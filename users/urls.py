from django.urls import path

from users.views import UserView, LoginJWTView

urlpatterns = [
    path("user/", UserView.as_view()),
    path("user/login/",LoginJWTView.as_view())
]