from django.urls import path, include
from . import views

from extract import views as ExtractViews

from card.views import CardView, CardDetailView

urlpatterns = [
    path("account/", views.AccountView.as_view()),
    path("account/<int:pk>/", views.AccountView.as_view()),
    path("account/<int:account_id>/", include("InvestmentCdi.urls")),

    path("account/<int:account_id>/operation", ExtractViews.CreateExtract.as_view()),

#VIEWS DE CARD
    path("account/card/", CardView.as_view()),
    path("account/card/<card_id>/", CardDetailView.as_view()),

]

