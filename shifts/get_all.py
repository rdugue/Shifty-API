from __future__ import print_function
import json
from utils import respond, get_all_shifts

def handler(event, context):
    print("Received api request: " + json.dumps(event, indent=2))

    if event['queryStringParameters']:
        params = event['queryStringParameters']
    else:
        params = {}
    if 'company' in params:
        response = get_all_shifts(params['company'])
        if 'error' in response:
            respond(response)
        else:
            respond(None, {'data': response['Items']})
    else:
        return respond({'error': 'No company specified'})
