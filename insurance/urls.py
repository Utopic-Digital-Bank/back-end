from django.urls import path, include

from . import views

urlpatterns = [
    path("insurance/", views.InsuranceViews.as_view()),
    path("insurance/<int:id>/",
          views.InsuranceDetailsViews.as_view()),
]

