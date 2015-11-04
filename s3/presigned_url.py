import jwt
import boto3

s3 = boto3.client('s3')

''' Input should be a JWT in the authorization header sent to API Gateway, payload looks like

{"user": "anything"}

Make sure to change the secret as well as put in your own bucket name.

'''

def generate_urls(event, context):
    input_data = jwt.decode(event['authorization'], 'changeme')
    print("user is {0}".format(input_data['user']))
    url = s3.generate_presigned_post('your bucket name here', '{0}/${{filename}}'.format(input_data['user']))

    return url
