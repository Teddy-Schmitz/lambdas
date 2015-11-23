import boto3
import random

#Put lots of random data into a dynamodb table

dynamodb = boto3.resource('dynamodb')
table_name = 'testing-dynamo'

def random_generator():
    table = dynamodb.Table(table_name)
    with table.batch_writer() as batch:
        for i in range(100):
            test_for = "blah{0}".format(i)
            for p in xrange(random.randint(666, 1234)):
                num_iterations = p
                batch.put_item(
                    Item={
                        'key': 'blah{0}-{1}'.format(p, test_for),
                        'for': test_for,
                        'result': 'testing'
                    }
                )
            print("This key {0} got {1} entries.".format(test_for, num_iterations))

if __name__ == "__main__":
    random_generator()