from __future__ import print_function
import json
from passlib.hash import bcrypt
from utils import respond, create_user, create_batch

def handler(event, context):
    print("Received api request: " + json.dumps(event, indent=2))

    if event['body']:
        payload = json.loads(event['body'])
        if type(payload) is list:
            users = []
            for user in payload:
                user['password'] = bcrypt.hash(user['password'])
                users.append(user)
            response = create_batch(users, 'User')
        else:
            payload['password'] = bcrypt.hash(payload['password'])
            response = create_user(payload)
        if 'error' in response:
            return respond(response)
        else:
            return respond(None, {'data': payload})
    else:
        return respond({'error': 'No request body'})