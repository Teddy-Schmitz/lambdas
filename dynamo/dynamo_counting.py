import boto3
from boto3.dynamodb.conditions import Key

#Counts the number of results for a certain key.

dynamodb = boto3.resource('dynamodb')

table_name = 'testing-dynamo'

def lambda_handler(event, context):
    table = dynamodb.Table(table_name)
    result = table.query(KeyConditionExpression=Key('for').eq('blah0'), Select='COUNT')
    return result['Count']
