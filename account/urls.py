from django.urls import path, include
from . import views

from InvestmentCdi import views as CdiViews
from card import views as CardViews
from extract import views as ExtractViews

urlpatterns = [
    path("account/", views.AccountView.as_view()),
    path("account/<int:pk>/", views.AccountDetails.as_view()),
    path("account/<int:account_id>/investment-cdi/",
         CdiViews.ListCreateInvestmentCdiView.as_view()),
    path("account/<int:account_id>/investment-cdi/<int:pk>/",
         CdiViews.InvestmentCdiDetailView.as_view()),
    path("account/card/", CardViews.CardView.as_view()),
    path("account/card/<int:card_id>/",
         CardViews.CardDetailView.as_view()),
    path("account/<int:pk>/operation/",
         ExtractViews.CreateExtract.as_view()),
    path("account/<int:account_id>/extract/",
         ExtractViews.ListExtract.as_view()),
]
