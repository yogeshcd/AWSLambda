import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('EMPLOYEES')

def lambda_handler(event, context):
    # TODO implement
    response = table.put_item(Item=event)
    return {"code" : 200, "message": "customer added sucessfuly"}
