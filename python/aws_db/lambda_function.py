# This file: python/awsquiz_get_questions/lambda_function.py
# To install a library in the current directory:
# pip3 install requests --target .

# @see https://docs.aws.amazon.com/code-library/latest/ug/python_3_dynamodb_code_examples.html
# @see https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/dynamodb
# @see https://dheeraj3choudhary.com/crud-operations-for-aws-dynamodb-using-python-boto3-script
# @see https://www.bitslovers.com/crud-with-python-and-dynamodb/

import boto3
import logging

logger = logging.getLogger(__name__)

import boto3
import logging

logger = logging.getLogger(__name__)

def lambda_handler(event, context):
    try:
        

        table_name = "awsquiz"

        category = event["category"]
        difficulty = event["difficulty"]
        set = event["set"]
        
        set_name = f"set::{set}::{difficulty}"

        # Initialize DynamoDB client
        dynamodb = boto3.resource('dynamodb')
        
        # Initialise table
        table = dynamodb.Table(table_name)
        
        # Do query using partion key and sort key
        resp = table.get_item(
            Key = {
                "category": category,
                "set_name": set_name
            }
        )

        if resp.get("Item") == None:

            logger.error(
                f'Questions not found, category={category}, set name={set_name}',
            )
                            
            return {
                'statusCode': 404
            }
        
        """
        {'category': 'entertainment', 'set_name': 'set::1::easy', 'questions': [{'question': 'Who is Darth Vader', 'answers': ['Sith Lord', 'Death Star butler'], 'correct_answer': 'Sith Lord'},
          {'question': 'Who destroyed the first Death Star', 'answers': ['Luke Skywalker', 'Some random stormtrooper who forgot to turn off the gas oven.'], 'correct_answer': 'Luke Skywalker'}]}
        """
        return {
            'statusCode':200,
            "category": category,
            "difficulty":difficulty,
            "set":"1",
            'questions':resp.get("Item")["questions"]
        }
        
        
    except Exception as err:

        logger.error(
            "%s %s %s %s ",
            "awsquiz",
            "1",
           "easy",
            str(err)
        )

        return {
            'statusCode': 500,
            'error': str(err),
            'event': str(event)
        }


if __name__ == "__main__":
    event = {
        "category": "entertainment",
        "difficulty": "easy",
        "set":1
    }
    response = lambda_handler(event, None)
    print(response)
