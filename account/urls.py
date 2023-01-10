from django.urls import path, include
from . import views

from insurance import views as InsuranceViews
from card import views as CardViews
from extract import views as ExtractViews

urlpatterns = [
    path("account/", views.AccountView.as_view()),
    path("account/<int:pk>/", views.AccountDetails.as_view()),
    path("account/<int:account_id>/", include("InvestmentCdi.urls")),
    path("account/card/", CardViews.CardView.as_view()),
    path("account/card/<int:card_int>/launch/",
         CardViews.CardDetailView.as_view()),
    path("account/<int:account_id>/operation/",
         ExtractViews.CreateExtract.as_view()),
    path("account/<int:account_id>/extract/",
         ExtractViews.ListExtract.as_view()),
]
