# Deploy-Lambda-function-to-create-weekly-EC2-AMI-backup!!
![Lambda-ami](https://user-images.githubusercontent.com/99130650/222965587-d14863b5-e79c-4083-bd56-ff5c3356f7c6.jpeg)

--------------------------------------------------


## Goal
Goals of this project to create weekly EC2 AMI backup of all EC2 instances running in the us-east-1 region and delete AMIs older than 30 days.

---------------------------------------------------

## Pre-Requisites
1- Deploy Lambda Function as per the architecture shown above with required IAM roles.

2- Schedule Lambda Function to run weekly once Sunday 5 AM EST using cloudwatch event as Lambda trigger.

3- Create 5 EC2 instances with Tags  as “Name: dpt-web-server”

4- Create SNS topic and subscribe e-mail to receive notifications.

---------------------------------------------------

## Description
This Python code is designed to create Amazon Machine Images (AMIs) for all EC2 instances in the us-east-1 region and delete old unused AMIs which are older than 30 days. It uses the Boto3 library to interact with the Amazon Web Services (AWS) EC2 and SNS (Simple Notification Service) APIs.

The code starts by initializing the EC2 and SNS clients and obtaining a list of all EC2 instances in the us-east-1 region. It then loops through the instances, creates an AMI for each instance, and adds tags to identify which AMI belongs to which EC2 instance. The AMI name is created using the instance name and the date when the AMI was created. The AMI description includes the instance name and the date when the AMI was created.

After creating the AMI, the code checks whether the AMI is older than 30 days. If it is, it checks whether the AMI is in use by checking whether it is attached to any running instances. If the AMI is not in use, the code deletes the AMI.

Finally, the code notifies an SNS topic if any exceptions occur during the process of creating or deleting AMIs.

To use this code, you can deploy it to an AWS Lambda function and schedule it to run at regular intervals using CloudWatch Events.

-------------------------------------------
## To deploy this code to a Lambda function, you can follow these steps:

1- Open the AWS Management Console and navigate to the Lambda service.

2- Click the "Create Function" button and choose the "Author from scratch" option.

3- Enter a name for your function and choose "Python 3.9" as the runtime.

4- Under "Permissions", choose "Create a new role with basic Lambda permissions".

5- Click the "Create function" button to create the function.

6- In the function editor, copy and paste the code above.

7- Set the SNS_TOPIC
