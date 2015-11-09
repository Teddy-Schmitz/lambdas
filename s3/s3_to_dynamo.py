import urllib
import boto3

s3 = boto3.client('s3')


def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key']).decode('utf8')
    try:
        meta = {}
        response = s3.get_object(Bucket=bucket, Key=key)
        print("CONTENT TYPE: " + response['ContentType'])

        if response['Metadata']:
            dynamodb = boto3.resource('dynamodb')
            table = dynamodb.Table('CHANGEME')
            for key, data in response['Metadata'].iteritems():
                #print("User metadata: key: {0} data: {1}".format(key, data))
                meta[key] = data

            table.put_item(Item={
                    'file-key': key,
                    'metadata': [meta]
                    })

        return 'OK'
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e