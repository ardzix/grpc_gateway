# api/serializers.py

from rest_framework import serializers

class ProcessPaymentSerializer(serializers.Serializer):
    user_id = serializers.CharField(max_length=100)
    amount = serializers.FloatField()
    currency = serializers.CharField(max_length=10)
    payment_method = serializers.CharField(max_length=50)

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
