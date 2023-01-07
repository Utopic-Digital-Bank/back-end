from django.urls import path, include

from . import views

urlpatterns = [
    path("economic-consultant/", views.EconomicConsultantView.as_view()),
]
