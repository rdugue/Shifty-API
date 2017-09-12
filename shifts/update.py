from __future__ import print_function
import json
from utils import respond, update_shift

def handler(event, context):
    print("Received api request: " + json.dumps(event, indent=2))

    if event['body']:
        payload = json.loads(event['body'])
        response = update_shift(payload)
        if 'error' in response:
            return respond(response)
        else:
            return respond(None, {'data': response['Attributes']})
    else:
        return respond({'error': 'No request body'})
