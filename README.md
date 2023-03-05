# Deploy-Lambda-function-to-create-weekly-EC2-AMI-backup!!
![Lambda-ami](https://user-images.githubusercontent.com/99130650/222965587-d14863b5-e79c-4083-bd56-ff5c3356f7c6.jpeg)



### Goal
Goals of this project to create weekly EC2 AMI backup of all EC2 instances running in the us-east-1 region and delete AMIs older than 30 days.

### Pre-Requisites
1- Deploy Lambda Function as per the architecture shown above with required IAM roles.
2- Schedule Lambda Function to run weekly once Sunday 5 AM EST using cloudwatch event as Lambda trigger.
3- Create 5 EC2 instances with Tags  as “Name: dpt-web-server”
4- Create SNS topic and subscribe e-mail to receive notifications.

## To deploy this code to a Lambda function, you can follow these steps:

1- Open the AWS Management Console and navigate to the Lambda service.

2- Click the "Create Function" button and choose the "Author from scratch" option.

3- Enter a name for your function and choose "Python 3.9" as the runtime.

4- Under "Permissions", choose "Create a new role with basic Lambda permissions".

5- Click the "Create function" button to create the function.

6- In the function editor, copy and paste the code above.

7- Set the SNS_TOPIC
