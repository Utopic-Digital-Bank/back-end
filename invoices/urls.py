from django.urls import path

from . import views
from invoices import views as invoices_views

urlpatterns = [
    path("card/<int:card_id>/invoices/", views.InvoiceView.as_view()),
    path("card/<int:card_id>/invoices/<int:pk>", invoices_views.InvoiceDetailView.as_view()),
]