from rest_framework import serializers
from google.protobuf.timestamp_pb2 import Timestamp
from datetime import datetime

class ItemSerializer(serializers.Serializer):
    item_name = serializers.CharField(max_length=100)
    quantity = serializers.IntegerField(min_value=1)
    price = serializers.FloatField(min_value=0)

class ProcessPaymentSerializer(serializers.Serializer):
    PAYMENT_METHOD_CHOICES = (
        ('OVO', 'Ovo e-wallet payment via Xendit'), 
        ('DANA', 'Dana e-wallet payment via Xendit'), 
        ('LINKAJA', 'Linkaja e-wallet payment via Xendit'), 
        ('BCA', 'BCA virtual account payment via Xendit'), 
        ('BNI', 'BNI virtual account payment via Xendit'), 
        ('BRI', 'BRI virtual account payment via Xendit'), 
        ('QR', 'QR Code (QRIS) payment via Xendit'), 
        ('DEFAULT', 'Xendit payment link'), 
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
    invoice_number = serializers.CharField(max_length=100)
    agent = serializers.CharField(max_length=100)
    items = ItemSerializer(many=True)

    def validate(self, data):
        if not data.get('items'):
            raise serializers.ValidationError("items is required and must have at least one item.")
        return data

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

class TimestampField(serializers.Field):
    def to_representation(self, value):
        # Convert Timestamp to ISO 8601 string
        if isinstance(value, Timestamp):
            dt = value.ToDatetime()
            return dt.isoformat()
        return value

    def to_internal_value(self, data):
        # Convert ISO 8601 string to Timestamp
        if isinstance(data, str):
            dt = datetime.fromisoformat(data)
            timestamp = Timestamp()
            timestamp.FromDatetime(dt)
            return timestamp
        return data

class PaymentSerializer(serializers.Serializer):
    payment_id = serializers.CharField(max_length=100)
    user_id = serializers.CharField(max_length=100)
    amount = serializers.FloatField()
    currency = serializers.CharField(max_length=10)
    payment_method = serializers.CharField(max_length=50)
    gateway = serializers.CharField(max_length=50)
    status = serializers.CharField(max_length=50)
    created_at = TimestampField()



class PaymentDetailSerializer(serializers.Serializer):
    payment_id = serializers.CharField(max_length=100)
    user_id = serializers.CharField(max_length=100)
    amount = serializers.FloatField()
    currency = serializers.CharField(max_length=10)
    payment_method = serializers.CharField(max_length=50)
    gateway = serializers.CharField(max_length=50)
    status = serializers.CharField(max_length=50)
    created_at = TimestampField()
    updated_at = TimestampField()
    phone_number = serializers.CharField(max_length=50, required=False)
    ewallet_checkout_method = serializers.CharField(max_length=50, required=False)
    qr_type = serializers.CharField(max_length=50, required=False)
    qr_callback_url = serializers.CharField(max_length=50, required=False)
    invoice_number = serializers.CharField(max_length=100)
    agent = serializers.CharField(max_length=100)
    items = ItemSerializer(many=True)

class ListPaymentsResponseSerializer(serializers.Serializer):
    payments = PaymentSerializer(many=True)
    total_count = serializers.IntegerField()
