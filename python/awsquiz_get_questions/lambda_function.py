# This file: python/awsquiz_get_questions/lambda_function.py
# To install a library in the current directory:
# pip3 install requests --target .
import requests
import uuid
import datetime
import hashlib

import logging

# @todo logging
logger = logging.getLogger(__name__)


def lambda_handler(event, context):
    try:
        
        category = event["category"]
        difficulty = event["difficulty"]
        set_number = event["set_number"]
        set_name = f"set::{set_number}::{difficulty}"
          
        return {
            "category":category,
            "set_name": set_name
        }
    
    
    except Exception as err:
        logger.error(
            "Error. %s: %s", 
            type(err).__name__, str(err)
        )

        return {
            'statusCode': 500,
            'error': str(err)
        }




if __name__ == "__main__":
    event = {
        "statusCode": 200,
        "category": "entertainment",
        "difficulty": "easy",
        "set_number":1
        

    }
