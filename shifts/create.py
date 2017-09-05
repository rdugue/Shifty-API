from __future__ import print_function
import json
from uuid import uuid4
from utils import respond, create

def handler(event, context):
    print("Received api request: " + json.dumps(event, indent=2))

    payload = json.loads(event['body'])
    if payload:
        payload['id'] = uuid4()
        payload['tradeable'] = False
        response = create(payload)
        if 'error' in response:
            return respond(response)
        else:
            return respond(None, {'data': payload})
    else:
        return respond({'error': 'No request body'})
