# api/grpc_client.py

import grpc
from payment.proto import payment_pb2_grpc, payment_pb2

class GRPCClient:
    def __init__(self, host='localhost', port=50051):
        self.channel = grpc.insecure_channel(f'{host}:{port}')
        self.stub = payment_pb2_grpc.PaymentServiceStub(self.channel)

    def process_payment(self, user_id, amount, currency, payment_method, *args, **kwargs):
        request = payment_pb2.ProcessPaymentRequest(
            user_id=user_id,
            amount=amount,
            currency=currency,
            payment_method=payment_method,
            ewallet_checkout_method=kwargs.get('ewallet_checkout_method'),
            qr_type=kwargs.get('qr_type'),
            qr_callback_url=kwargs.get('qr_callback_url')
        )
        return self.stub.ProcessPayment(request)

    def get_payment_status(self, payment_id):
        request = payment_pb2.GetPaymentStatusRequest(payment_id=payment_id)
        return self.stub.GetPaymentStatus(request)

    def list_payments(self, user_id, page, page_size):
        request = payment_pb2.ListPaymentsRequest(
            user_id=user_id,
            page=page,
            page_size=page_size
        )
        return self.stub.ListPayments(request)

