'''
This file is for implementing API response method and database helper methods.
'''
from __future__ import print_function # Python 2/3 compatibility
import json
import boto3
from botocore.exceptions import ClientError

dynamo = boto3.resource('dynamodb')

def respond(err, res=None):
    return {
        'statusCode': 400 if err else 200,
        'body': json.dumps(err or res),
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True,
            'Content-Type': 'application/json',
        },
    }

def get_user(userId, company):
    try:
        table = dynamo.Table('Users')
        response = table.get_item(
            Key={
                'userId': userId,
                'company': company
            }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
        return {'error': e.response['Error']['Message']}
    else:
        return response

def create(item):
    try:
        table = dynamo.Table('Shifts')
        response = table.put_item(
            Item=item,
            ReturnValues='ALL_OLD'
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
        return {'error': e.response['Error']['Message']}
    else:
        return response

def update_shift(shift):
    try:
        table = dynamo.Table('Shifts')
        response = table.update_item(
            Key={
                'id': shift['id']
            },
            UpdateExpression='SET #c = :c, #e = :e, #s = :s, #et = :et, #d = :d, #t = :t',
            ExpressionAttributeNames={
                '#c': 'company',
                '#e': 'employee',
                '#s': 'start',
                '#et': 'end',
                '#d': 'day',
                '#t': 'tradeable'
            },
            ExpressionAttributeValues={
                ':c': shift['company'],
                ':e': shift['employee'],
                ':s': shift['start'],
                ':et': shift['end'],
                ':d': shift['day'],
                ':t': shift['tradeable']
            },
            ReturnValues="ALL_NEW"
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
        return {'error': e.response['Error']['Message']}
    else:
        return response

def delete_shift(ids):
    try:
        table = dynamo.Table('Shifts')
        response = table.delete_item(
            Key={
                'id': ids
            },
            ReturnValues='ALL_OLD'
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
        return {'error': e.response['Error']['Message']}
    else:
        return response

def get_shifts_by_day(company, day):
    try:
        table = dynamo.Table('Shifts')
        response = table.scan(
            FilterExpression="#d = :d AND company = :c",
            ExpressionAttributeNames={
                "#d": 'day'
            },
            ExpressionAttributeValues={
                ":d": day,
                ":c": company
            },
            ConsistentRead=True
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
        return {'error': e.response['Error']['Message']}
    else:
        return response

def get_all_shifts(company):
    try:
        table = dynamo.Table('Shifts')
        response = table.scan(
            FilterExpression="company = :c",
            ExpressionAttributeValues={
                ":c": company
            },
            ConsistentRead=True
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
        return {'error': e.response['Error']['Message']}
    else:
        return response

def get_all_trades(company):
    try:
        table = dynamo.Table('Shifts')
        response = table.scan(
            FilterExpression="tradeable = :t AND company = :c",
            ExpressionAttributeValues={
                ":t": True,
                ":c": company
            },
            ConsistentRead=True
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
        return {'error': e.response['Error']['Message']}
    else:
        return response

def get_trades_by_day(company, day):
    try:
        table = dynamo.Table('Shifts')
        response = table.scan(
            FilterExpression="#d = :d, tradeable = :t AND company = :c",
            ExpressionAttributeNames={
                "#d": 'day'
            },
            ExpressionAttributeValues={
                ":d": day,
                ":t": True,
                ":c": company
            },
            ConsistentRead=True
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
        return {'error': e.response['Error']['Message']}
    else:
        return response
