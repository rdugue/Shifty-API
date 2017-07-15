from __future__ import print_function
import json
from utils import respond, get_shifts_by_day

def handler(event, context):
    print("Received api request: " + json.dumps(event, indent=2))

    if event['pathParameters']:
        params = event['pathParameters']
    else:
        params = {}
    if 'company' in params:
        if 'day' in params:
            response = get_shifts_by_day(params['company'], params['day'])
            if 'error' in response:
                return respond(response)
            else:
                return respond(None, {'data': response['Items']})
        else:
            return respond({'error': 'No day specified'})
    else:
        return respond({'error': 'No company specified'})
