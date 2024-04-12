# This file: python/awsquiz_invoke_state_machine/lambda_function.py
# To install a library in the current directory:
# pip3 install requests --target .
# @see https://kashyapgohil25.medium.com/how-to-invoke-the-step-function-from-lambda-7ff0b7812554
# @ see https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-api-gateway.html

import boto3
import json


def lambda_handler(event, context):

    try:

        # Role = arn:aws:iam::881617337234:role/APIGatewayToStepFunctions
        # State machine = arn:aws:states:ap-southeast-2:881617337234:stateMachine:MyStateMachine-di9jzahp0

        sf = boto3.client('stepfunctions', region_name = 'ap-southeast-2')
        input_dict = {'category': "entertainment", 'difficulty':"easy", 'set':1}
        execution_result = sf.start_execution(
            stateMachineArn = 'arn:aws:states:ap-southeast-2:881617337234:stateMachine:MyStateMachine-di9jzahp0',
            input = json.dumps(input_dict)
        )

        response = sf.describe_execution(
            executionArn = execution_result['executionArn']
        )
        
        return response
    
    
    except Exception as err:

        return {
            'statusCode': 500,
            'error': str(err)
        }


if __name__ == "__main__":
    print("Start")
    response = lambda_handler(None, None)
    print(response)
    print("end")
