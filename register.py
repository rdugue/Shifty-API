from __future__ import print_function
from datetime import datetime, timedelta
import json
import boto3
import jwt
from passlib.hash import pbkdf2_sha256
from botocore.exceptions import ClientError
from utils import respond, create

print('Loading function')
dynamo = boto3.resource('dynamodb')
JWT_SECRET = 'secret'
JWT_ALGORITHM = 'HS256'
JWT_EXP_DELTA_SECONDS = 60*60*24*2

def handler(event, context):
    print("Received registration attempt: " + json.dumps(event, indent=2))
    if event['body']:
        user = json.loads(event['body'])
    else:
        return respond({'error': 'no POST body'})
    user['password'] = pbkdf2_sha256.hash(user['password'])
    response = create(user, 'users')
    if 'error' not in response:
        jwt_payload = {
            'userId': user['userId'],
            'position': user['position'],
            'company': user['company'],
            'exp': datetime.utcnow() + timedelta(seconds=JWT_EXP_DELTA_SECONDS)
        }
        jwt_token = jwt.encode(jwt_payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
        print("Registration succeeded: " + json.dumps(response, indent=2))
        return respond(None, {
            'token': jwt_token.decode(),
            'data': user
            })
    else:
        print("Registration failed: " + json.dumps(response, indent=2))
        return respond(response)
        