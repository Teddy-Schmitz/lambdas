import boto3

""" lambda to share ami images by image id or by tag"""

ec2 = boto3.resource('ec2')


def lambda_handler_by_id(event, context):
    user = event['user']
    image_id = event['image_id']
    image = ec2.Image(image_id)
    image.modify_attribute(LaunchPermission={
        'Add': [
            {
                'UserId': user
            }
        ]})
    return 'OK'

def lambda_handler_by_tag(event, context):
    client = boto3.client('ec2')
    user = event['user']
    tag = event['tag']

    image_list = client.describe_images(Filters=[
        {
            'Name': 'tag-value',
            'Values': [
                tag
            ]
        },
    ])

    if len(image_list['Images']) > 1:
        raise Exception('Tag should be unique')

    image_id = image_list['Images'][0]['ImageId']

    image = ec2.Image(image_id)
    image.modify_attribute(LaunchPermission={
        'Add': [
            {
                'UserId': user
            }
        ]})
    return 'OK'
