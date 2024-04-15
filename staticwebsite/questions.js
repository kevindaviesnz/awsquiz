// creating an array and passing the number, questions, options, and answers
// @see https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API

/*
{"statusCode": 200, "category": "entertainment", "difficulty": "easy", "set": "1", "questions": [{"question": "Who is Darth Vader", "answers": ["Sith Lord", "Death Star butler"], "correct_answer": "Sith Lord"}, {"question": "Who destroyed the first Death Star", "answers": ["Luke Skywalker", "Some random stormtrooper who forgot to turn off the gas oven."], "correct_answer": "Luke Skywalker"}]}
*/

async function fetchQuestions() {
  const response = await fetch("http://localhost:8080/example.json");
  const json = await response.json();
  console.log(json["questions"]);
  // Map questions to get the expected format
  questions = json["questions"].map((question_set, i) => {
  
  })
}

fetchQuestions()

let questions = [
    {
    numb: 1,
    question: "What does HTML stand for?",
    answer: "Hyper Text Markup Language",
    options: [
      "Hyper Text Preprocessor",
      "Hyper Text Markup Language",
      "Hyper Text Multiple Language",
      "Hyper Tool Multi Language"
    ]
  },
    {
    numb: 2,
    question: "What does CSS stand for?",
    answer: "Cascading Style Sheet",
    options: [
      "Common Style Sheet",
      "Colorful Style Sheet",
      "Computer Style Sheet",
      "Cascading Style Sheet"
    ]
  },
    {
    numb: 3,
    question: "What does PHP stand for?",
    answer: "Hypertext Preprocessor",
    options: [
      "Hypertext Preprocessor",
      "Hypertext Programming",
      "Hypertext Preprogramming",
      "Hometext Preprocessor"
    ]
  },
    {
    numb: 4,
    question: "What does SQL stand for?",
    answer: "Structured Query Language",
    options: [
      "Stylish Question Language",
      "Stylesheet Query Language",
      "Statement Question Language",
      "Structured Query Language"
    ]
  },
    {
    numb: 5,
    question: "What does XML stand for?",
    answer: "eXtensible Markup Language",
    options: [
      "eXtensible Markup Language",
      "eXecutable Multiple Language",
      "eXTra Multi-Program Language",
      "eXamine Multiple Language"
    ]
  },
  // you can uncomment the below codes and make duplicate as more as you want to add question
  // but remember you need to give the numb value serialize like 1,2,3,5,6,7,8,9.....

  //   {
  //   numb: 6,
  //   question: "Your Question is Here",
  //   answer: "Correct answer of the question is here",
  //   options: [
  //     "Option 1",
  //     "option 2",
  //     "option 3",
  //     "option 4"
  //   ]
  // },
];



