from __future__ import print_function
import json
from utils import delete_shift, respond

def handler(event, context):
    print("Received api request: " + json.dumps(event, indent=2))

    if event['pathParameters']:
        params = event['pathParameters']
        if 'id' not in params:
            return respond({'error': 'shift id not specified'})
        else:
            response = delete_shift(params['id'])
            if 'error' in response:
                return respond(response)
            else:
                return respond(None, {'data': response['Attributes']})
    else:
        return respond({'error': 'this will never happen probably...'})