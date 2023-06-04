import json
import boto3
import ast

def lambda_handler(event, context):
    # TODO implement
    object_key = event['Records'][0]['s3']['object']['key']
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    print(f"bucket name: {bucket_name} and object name: {object_key}")
    s3 = boto3.client('s3', region_name='ap-south-1')
    response = s3.get_object(Bucket = bucket_name, Key = object_key)
    file_reader = response['Body'].read().decode("utf-8")
    file_reader2 = ast.literal_eval(file_reader)
    dynamodb_client = boto3.resource('dynamodb')
    table = dynamodb_client.Table('user')
    table.put_item(Item=file_reader)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }