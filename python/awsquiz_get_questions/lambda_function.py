# This file: python/awsquiz_get_questions/lambda_function.py
# To install a library in the current directory:
# pip3 install requests --target .

def lambda_handler(event, context):
    try:
        
        category = event["category"]
        difficulty = event["difficulty"]
        set = event["set"]
        set_name = f"set::{set}::{difficulty}"
          
        return {
            "category":category,
            "set_name": set_name
        }
    
    
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
