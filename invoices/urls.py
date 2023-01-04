from django.urls import path

from . import views
from invoices import views as invoices_views

urlpatterns = [
    path("invoices/", views.InvoiceView.as_view()),
    path("invoices/<int:pk>/", invoices_views.InvoiceView.as_view()),
]