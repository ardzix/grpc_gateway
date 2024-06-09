python -m grpc_tools.protoc -I api/proto --python_out=api/proto --grpc_python_out=api/proto api/proto/payment.proto

rename `payment_pb2_grpc.py` import to from . import payment_pb2 as payment__pb2