## Questions

> GET http:...

Get sets of questions.

> **Parameters**                                    
category | string, category of questions to get \
difficulty | string, difficulty (easy, medium, hard) \
set_number  | int, the set number.

#### Example
http:...?category=entertainment&difficulty=easy&set_number=1

` 
code
{
    "entertainment": {
        "set_count": 2,
        "set::1::easy": {
            "questions": [
                {
                    "question": "Who is Darth Vader?",
                    "answers": [
                        "Sith Lord",
                        "Death Star butler"
                    ],
                    "correct_answer": "Sith Lord"
                },
                {
                    "question": "Who destroyed the first Death Star?",
                    "answers": [
                        "Luke Skywalker",
                        "Some random stormtrooper who forgot to turn off the gas oven"
                    ],
                    "correct_answer": "Luke Skywalker"
                },
                {
                    "question": "Which movie won best picture in 2024?",
                    "answers": [
                        "Oppenheimer",
                        "Barbie",
                        "Joe Dirt"
                    ],
                    "correct_answer": "Oppenheimer"
                },
                {
                    "question": "In 'Oppenheimer', what's the main conflict?",
                    "answers": [
                        "Nuclear warfare",
                        "Oppenheimer's love for chemistry set",
                        "Alien invasion"
                    ],
                    "correct_answer": "Nuclear warfare"
                }
            ]
        },
    }
}
 `
