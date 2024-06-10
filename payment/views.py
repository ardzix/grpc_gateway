# api/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg import openapi  # Import openapi
from drf_yasg.utils import swagger_auto_schema
from .grpc_client import GRPCClient
from .serializers import (
    ProcessPaymentSerializer, ProcessPaymentResponseSerializer,
    GetPaymentStatusSerializer, GetPaymentStatusResponseSerializer,
    ListPaymentsSerializer, ListPaymentsResponseSerializer
)


# api/views.py

class ProcessPaymentView(APIView):
    @swagger_auto_schema(
        request_body=ProcessPaymentSerializer,
        responses={
            200: openapi.Response(
                description="Payment processed successfully",
                schema=ProcessPaymentSerializer,
            )
        },
    )
    def post(self, request):
        serializer = ProcessPaymentSerializer(data=request.data)
        if serializer.is_valid():
            client = GRPCClient()
            response = client.process_payment(**serializer.validated_data)
            response_serializer = ProcessPaymentResponseSerializer({
                'payment_id': response.payment_id,
                'status': response.status
            })
            return Response(response_serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetPaymentStatusView(APIView):
    @swagger_auto_schema(
        responses={200: GetPaymentStatusResponseSerializer},
        manual_parameters=[
            openapi.Parameter('payment_id', openapi.IN_PATH, description="Payment ID", type=openapi.TYPE_STRING)
        ]
    )
    def get(self, request, payment_id):
        serializer = GetPaymentStatusSerializer(data={'payment_id': payment_id})
        if serializer.is_valid():
            client = GRPCClient()
            response = client.get_payment_status(payment_id)
            response_serializer = GetPaymentStatusResponseSerializer({
                'payment_id': response.payment_id,
                'status': response.status,
                'error_message': response.error_message
            })
            return Response(response_serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListPaymentsView(APIView):
    @swagger_auto_schema(
        query_serializer=ListPaymentsSerializer,
        responses={200: ListPaymentsResponseSerializer}
    )
    def get(self, request):
        serializer = ListPaymentsSerializer(data=request.query_params)
        if serializer.is_valid():
            client = GRPCClient()
            response = client.list_payments(**serializer.validated_data)
            response_serializer = ListPaymentsResponseSerializer({
                'payments': response.payments,
                'total_count': response.total_count
            })
            return Response(response_serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
