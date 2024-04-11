# This file: python/awsquiz_get_questions/lambda_function.py
# To install a library in the current directory:
# pip3 install requests --target .

# @see https://docs.aws.amazon.com/code-library/latest/ug/python_3_dynamodb_code_examples.html
# @see https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/dynamodb
# @see https://dheeraj3choudhary.com/crud-operations-for-aws-dynamodb-using-python-boto3-script
# @see https://www.bitslovers.com/crud-with-python-and-dynamodb/

import boto3

def lambda_handler(event, context):
    try:
        
        table_name = "awsquiz"
        partition_key = "category"
        sort_key = "set:1:easy"
        
        # Initialize DynamoDB client
        dynamodb = boto3.resource('dynamodb')
        
        # Initialise table
        table = dynamodb.Table(table_name)
        
        # Do query using partion key and sort key
        
    
    except Exception as err:

        return {
            'statusCode': 500,
            'error': str(err)
        }




if __name__ == "__main__":
    event = {
        "statusCode": 200,
        "category": "entertainment",
        "difficulty": "easy",
        "set":1
    }
