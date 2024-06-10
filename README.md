
# gRPC Gateway

## Overview

The gRPC Gateway is a RESTful API gateway for the Payment Service. It is written in Python using Django and Django REST framework. It allows users to interact with the gRPC-based Payment Service via RESTful endpoints.

## Prerequisites

- Python 3.9 or later
- Docker (optional, for containerized deployment)

## Setup

### 1. Clone the repository

```sh
git clone <repository-url>
cd grpc_gateway
```

### 2. Install dependencies

```sh
pip install -r requirements.txt
```

### 3. Run the Django server

#### Locally

```sh
python manage.py runserver
```

#### Using Docker

Build the Docker image:

```sh
docker build -t grpc_gateway .
```

Run the Docker container:

```sh
docker run -p 8000:8000 grpc_gateway
```

## Environment Variables

Create a `.env` file to configure the following environment variables:

- `PAYMENT_SERVICE_HOST`: Host of the payment service
- `PAYMENT_SERVICE_PORT`: Port of the payment service

## Usage

The gRPC Gateway exposes the following RESTful endpoints:

- `POST /api/payment/process_payment`
- `GET /api/payment/get_payment_status`
- `GET /api/payment/list_payments`
- `GET /api/payment/get_payment_detail`

Refer to the Django views and serializers for more details on the request and response formats.

## License

This project is licensed under the MIT License.