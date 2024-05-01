import argparse
import json

def convert_to_dynamodb_json(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    questions = []
    current_question = {}
    in_question = False
    in_answers = False
    in_correct = False
    in_explanation = False

    for line in lines:
        line = line.strip()
        if line.startswith("[q]"):
            in_question = True
            in_answers = False
            in_correct = False
            in_explanation = False
            if current_question:
                questions.append(current_question)
            current_question = {"question": "", "answers": [], "correct_answer": [], "explanation":""}
        elif line.startswith("[answers]"):
            in_question = False
            in_answers = True
            in_correct = False            
        elif line.startswith("[correct]"):
            in_question = False
            in_answers = False
            in_correct = True 
            in_explanation = False           
        elif line.startswith("[explanation]"):
            in_question = False
            in_answers = False
            in_correct = False
            in_explanation = True
        elif in_question:
            current_question["question"] += line + "\n"
        elif in_answers and line:
            current_question["answers"].append(line)
        elif in_correct and line:
            current_question["correct_answer"].append(line)
        elif in_explanation and line:
            current_question["explanation"] += line + "\n"

    # Append the last question
    if current_question:
        questions.append(current_question)

    dynamodb_json = {
        "category": {"S": "aws"},  # Adjust this as needed
        "set_name": {"S": "set::1::easy"},  # Adjust this as needed
        "questions": {"L": []}
    }

    for question in questions:
        dynamodb_json["questions"]["L"].append({
            "M": {
                "question": {"S": question["question"].strip()},
                "answers": {"L": [{"S": answer} for answer in question["answers"]]},
                "correct_answer": {"L": [{"S": ans} for ans in question.get("correct_answer", [])]},  # Ensure correct_answer is added
                "explanation": {"S": question["explanation"].strip()},
            }
        })

    with open(output_file, 'w') as f:
        json.dump(dynamodb_json, f, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert formatted text file to DynamoDB JSON format")
    parser.add_argument("input_file", help="Path to the input text file")
    parser.add_argument("output_file", help="Path to the output JSON file")
    args = parser.parse_args()

    convert_to_dynamodb_json(args.input_file, args.output_file)
