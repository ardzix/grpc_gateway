python -m grpc_tools.protoc -I payment/proto --python_out=payment/proto --grpc_python_out=payment/proto payment/proto/payment.proto

rename `payment_pb2_grpc.py` import to from . import payment_pb2 as payment__pb2