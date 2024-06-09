# api/urls.py

from django.urls import path
from .views import ProcessPaymentView, GetPaymentStatusView, ListPaymentsView

urlpatterns = [
    path('process_payment/', ProcessPaymentView.as_view(), name='process_payment'),
    path('payment_status/<str:payment_id>/', GetPaymentStatusView.as_view(), name='payment_status'),
    path('list_payments/', ListPaymentsView.as_view(), name='list_payments'),
]
