import json
import boto3

client = boto3.client('ec2')
def lambda_handler(event, context):
    # TODO implement
    response = client.describe_instances()
    
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            id = [instance["InstanceId"]]
            
            if instance["State"]["Name"] == "running":
                client.stop_instances(InstanceIds=id)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
