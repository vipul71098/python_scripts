import boto3
import json

client = boto3.client('secretsmanager')

response = client.put_secret_value(
    SecretId='DatabaseProdSecrets',
    SecretString='{"username": "tester", "password": "test-world-updated2"}'
)

print(response)
