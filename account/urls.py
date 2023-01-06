from django.urls import path
from . import views

urlpatterns = [
    path("account/", views.AccountView.as_view()),
    path("account/<int:pk>/", views.AccountView.as_view()),
    # path("account/insurance/", #Views de insurance#,
    # path("account/economic_consultant/ #Views de account#")#

]