# api/urls.py

from django.urls import path
from .views import ProcessPaymentView, GetPaymentStatusView, ListPaymentsView, GetPaymentDetailView

urlpatterns = [
    path('process_payment/', ProcessPaymentView.as_view(), name='process_payment'),
    path('list_payments/', ListPaymentsView.as_view(), name='list_payments'),
    path('payment_status/<str:payment_id>/', GetPaymentStatusView.as_view(), name='payment_status'),
    path('payment_detail/<str:payment_id>/', GetPaymentDetailView.as_view(), name='payment_detail'),
]
