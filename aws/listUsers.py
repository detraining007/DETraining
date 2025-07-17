import boto3

def list_iam_users():
    # Create an IAM client
    iam = boto3.client('iam')
    # List IAM users
    response = iam.list_users()
    # Print user names
    for user in response['Users']:
        print(user['UserName'])

list_iam_users()

# print("code executed sucessfully")