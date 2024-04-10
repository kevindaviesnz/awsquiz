# This file: python/awsquiz_invoke_state_machine/lambda_function.py
# To install a library in the current directory:
# pip3 install requests --target .

import logging

# @todo logging
logger = logging.getLogger(__name__)

def lambda_handler(event, context):
    try:
        
        return {
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
    pass