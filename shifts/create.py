from __future__ import print_function
import json
from uuid import uuid4
from utils import respond, create, create_batch

def handler(event, context):
    print("Received api request: " + json.dumps(event, indent=2))

    if event['body']:
        payload = json.loads(event['body'])
        if type(payload) is list:
            shifts = []
            for shift in payload:
                shift['id'] = str(uuid4())
                shift['tradeable'] = False
                shifts.append(shift)
            response = create_batch(shifts, 'Shifts')
        else:
            payload['id'] = str(uuid4())
            payload['tradeable'] = False
            response = create(payload)
        if 'error' in response:
            return respond(response)
        else:
            return respond(None, {'data': payload})
    else:
        return respond({'error': 'No request body'})
