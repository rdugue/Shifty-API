from __future__ import print_function
import json
from utils import respond, get_user

def handler(event, context):
    print("Received api request: " + json.dumps(event, indent=2))

    if event['pathParameters']:
        params = event['pathParameters']
    else:
        params = {}
    if 'userId' in params:
        response = get_user(params['userId'])
        if 'Item' in response:
            return respond(None, {'data': response['Item']})
        else:
            return respond(response)
    else:
        return respond({'error': 'Invalid user path'})
    