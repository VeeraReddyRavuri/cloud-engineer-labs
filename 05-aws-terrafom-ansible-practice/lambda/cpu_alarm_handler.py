 import boto3

def handler(event, context):
    print(f"Cpu alarm triggered: {event}")

    s3 = boto3.client('s3')
    s3.put_object(
        Bucket = 'your-bucket',
        Key = f'alarms/{context.aws_request_id}.json',
        Body = str(event)
    )