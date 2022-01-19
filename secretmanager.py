import boto3

client = boto3.client('secretsmanager')

response = client.create_secret(
    Name='DatabaseSecrets',
    SecretString='{"username": "prod", "password": "hello-world-prod"}'
)