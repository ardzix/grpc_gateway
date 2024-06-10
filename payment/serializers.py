# api/serializers.py

from rest_framework import serializers

class ProcessPaymentSerializer(serializers.Serializer):
    PAYMENT_METHOD_CHOICES = (
        ('XEN-OVO', 'Ovo e-wallet payment via Xendit'), 
        ('XEN-DANA', 'Dana e-wallet payment via Xendit'), 
        ('XEN-LINKAJA', 'Linkaja e-wallet payment via Xendit'), 
        ('XEN-BCA', 'BCA virtual account payment via Xendit'), 
        ('XEN-BNI', 'BNI virtual account payment via Xendit'), 
        ('XEN-BRI', 'BRI virtual account payment via Xendit'), 
        ('XEN-QR', 'QR Code (QRIS) payment via Xendit'), 
        ('XEN-DEFAULT', 'Xendit payment link'), 
    )
    QR_TYPE_CHOICES = (
        ('DYNAMIC', 'Dynamic QR payment'), 
        ('STATIC', 'Static QR payment')
    )
    user_id = serializers.CharField(max_length=100)
    amount = serializers.FloatField()
    currency = serializers.CharField(max_length=10)
    payment_method = serializers.ChoiceField(choices=PAYMENT_METHOD_CHOICES)
    ewallet_checkout_method = serializers.CharField(max_length=50, required=False)
    qr_type = serializers.ChoiceField(required=False, choices=QR_TYPE_CHOICES)
    qr_callback_url = serializers.CharField(max_length=50, required=False)

class ProcessPaymentResponseSerializer(serializers.Serializer):
    payment_id = serializers.CharField(max_length=100)
    status = serializers.CharField(max_length=50)

class GetPaymentStatusSerializer(serializers.Serializer):
    payment_id = serializers.CharField(max_length=100)

class GetPaymentStatusResponseSerializer(serializers.Serializer):
    payment_id = serializers.CharField(max_length=100)
    status = serializers.CharField(max_length=50)
    error_message = serializers.CharField(max_length=200, required=False)

class ListPaymentsSerializer(serializers.Serializer):
    user_id = serializers.CharField(max_length=100)
    page = serializers.IntegerField(min_value=1, default=1)
    page_size = serializers.IntegerField(min_value=1, default=10)

class PaymentSerializer(serializers.Serializer):
    payment_id = serializers.CharField(max_length=100)
    user_id = serializers.CharField(max_length=100)
    amount = serializers.FloatField()
    currency = serializers.CharField(max_length=10)
    status = serializers.CharField(max_length=50)
    created_at = serializers.CharField(max_length=50)

class ListPaymentsResponseSerializer(serializers.Serializer):
    payments = PaymentSerializer(many=True)
    total_count = serializers.IntegerField()
