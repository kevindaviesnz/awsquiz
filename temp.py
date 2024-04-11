
import json

def lambda_handler(event, context):
    # Extract the items from the DynamoDB response
    items = event["Items"]

    # Assuming your Lambda function processes the input and generates some output
    # For example, let's just extract the first question for demonstration
    if len(items) > 0:
        first_question = items[0]["questions"]["L"][0]["M"]
        question_text = first_question["question"]["S"]
        answers = [answer["S"] for answer in first_question["answers"]["L"]]
        correct_answer = first_question["correct_answer"]["S"]

        output_data = {
            "question": "to be or not to be",
            "answers": answers,
            "correct_answer": correct_answer
        }
    else:
        output_data = {
            "message": "No questions found in DynamoDB"
        }

    # Return the output in a format that can be passed back through API Gateway
    """
        return {
        "statusCode": 200,
        "body": json.dumps(output_data),
        "headers": {
            "Content-Type": "application/json"
        }
    }
    
    """

    return {
        "id": 1,
        "type": "dog",
        "price": 249.99
      }

