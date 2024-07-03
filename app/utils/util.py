import jwt
import os
from datetime import datetime, timedelta, timezone


# Create a secret key constant
SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'


def encode_token(customer_id):
    payload = {
        'exp': datetime.now(timezone.utc) + timedelta(hours=1),
        'iat': datetime.now(timezone.utc),
        'customer_id': customer_id
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token
