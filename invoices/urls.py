from django.urls import path

from . import views
from invoices import views as invoices_views

urlpatterns = [
    path("invoices/<int:pk>/", invoices_views.InvoiceDetailView.as_view()),
]