from django.urls import path

from users.views import UserView, LoginJWTView, UserDetailView

urlpatterns = [
    path("user/", UserView.as_view()),
    path("user/login/",LoginJWTView.as_view()),
    path("user/<user_id>/", UserDetailView.as_view()),
]