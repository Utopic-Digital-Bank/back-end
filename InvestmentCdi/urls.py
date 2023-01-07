from django.urls import path, include

from . import views

urlpatterns = [
    path("investment-cdi/", views.ListCreateInvestmentCdiView.as_view()),
    path("investment-cdi/<int:pk>/",
         views.InvestmentCdiDetailView.as_view()),
]