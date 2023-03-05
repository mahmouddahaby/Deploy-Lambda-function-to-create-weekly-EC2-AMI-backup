import boto3
from datetime import datetime, timedelta
import os

# Create EC2 client
ec2_client = boto3.client('ec2', region_name='us-east-1')

# Create SNS client
sns_client = boto3.client('sns')

# Get list of all EC2 instances in us-east-1 region
ec2_instances = ec2_client.describe_instances()

# Get list of EC2 Instance Ids as list data type
instance_ids = []
for reservation in ec2_instances['Reservations']:
    for instance in reservation['Instances']:
        instance_ids.append(instance['InstanceId'])

# Get the EC2 Tag having key “Name”
for reservation in ec2_instances['Reservations']:
    for instance in reservation['Instances']:
        for tag in instance['Tags']:
            if tag['Key'] == 'Name':
                name_tag = tag['Value']
                break

# Loop the list of Instance Ids and create AMI
for instance_id in instance_ids:
    # Add tags to the AMI
    name = ec2_client.describe_tags(Filters=[{'Name': 'resource-id','Values': [instance_id]},{'Name': 'key','Values': ['Name']}])['Tags'][0]['Value']
    now = datetime.now()
    date_string = now.strftime('%Y-%m-%d')
    image_name = f"{name}-{date_string}"
    description = f"AMI for {name} created on {date_string}"
    response = ec2_client.create_image(InstanceId=instance_id, Name=image_name, Description=description, NoReboot=True)
    ami_id = response['ImageId']
    print(f"Created AMI with id {ami_id} for instance {instance_id}")

    # Add tags to the AMI
    response = ec2_client.create_tags(Resources=[ami_id], Tags=[{'Key': 'Name', 'Value': name}])

    # Delete the old unused AMIs which are older than 30 days from the date of AMI creation
    ami_creation_date = datetime.strptime(response['CreationDate'], '%Y-%m-%dT%H:%M:%S.%fZ')
    ami_age = datetime.now() - ami_creation_date
    if ami_age > timedelta(days=30):
        response = ec2_client.describe_images(ImageIds=[ami_id])
        if len(response['Images'][0]['BlockDeviceMappings']) == 0:
            response = ec2_client.deregister_image(ImageId=ami_id)
            print(f"Deleted AMI with id {ami_id}")
        else:
            print(f"AMI with id {ami_id} is in use and cannot be deleted.")

# Notify to SNS topic if any exceptions in creating or deleting AMI
try:
    # Publish a message to the specified SNS topic
    topic_arn = os.environ['SNS_TOPIC_ARN']
    sns_client.publish(TopicArn=topic_arn, Message="Successfully created and deleted AMIs.")
except Exception as e:
    print(f"Error publishing message to SNS topic: {e}")

