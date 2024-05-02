// creating an array and passing the number, questions, options, and answers
// @see https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API

/*
{"statusCode": 200, "category": "entertainment", "difficulty": "easy", "set": "1", 
"questions": [
  {
    "question": "Who is Darth Vader", 
    "answers": ["Sith Lord", "Death Star butler"],
 "correct_answer": "Sith Lord"}, {"question": "Who destroyed the first Death Star", "answers": ["Luke Skywalker", "Some random stormtrooper who forgot to turn off the gas oven."], "correct_answer": "Luke Skywalker"}]}
*/
var showQuestionSet = null

async function fetchQuestions() {
  
  uri = "https://ka1iduxaf3.execute-api.ap-southeast-2.amazonaws.com/dev/fetch-questions?category=awscpe&set=1&difficulty=hard"
  //uri = "https://jit6rh5po1.execute-api.ap-southeast-2.amazonaws.com/dev/fetch-questions?category=aws&set=1&difficulty=easy"
  //uri = "https://0x3ns0i81h.execute-api.ap-southeast-2.amazonaws.com/dev/fetch-questions?category=general&set=1&difficulty=easy"
  const response = await fetch(uri);
  const json = await response.json();
  json.questions.sort(() => Math.random() - 0.5);
  
  // Map questions to get the expected format
  questions = json["questions"].slice(0,65).map((question_set, i) => {
    return {
      "numb": i + 1,
      "question": question_set["question"],
      "options": question_set["answers"],
      "answer": question_set["correct_answer"][0],
      "explanation": question_set["explanation"],

    }
  })

  console.log("Got " + questions.length + " questions");

  // Here we create a closure, call it immediately, and return it as a function.
  showQuestionSet = ((qs) => {
   return (index) => {
     // Was showQuetions(index)
     const que_text = document.querySelector(".que_text");
     const que_explanation = document.querySelector(".que_explanation");
      //creating a new span and div tag for question and option and passing the value using array index
      let que_tag = '<span>' + qs[index].numb + ". " + qs[index].question + '</span>';
      let option_tag = '<div class="option"><span>' + qs[index].options[0] + '</span></div>'
          + '<div class="option"><span>' + qs[index].options[1] + '</span></div>'
          + '<div class="option"><span>' + qs[index].options[2] + '</span></div>'
          + '<div class="option"><span>' + qs[index].options[3] + '</span></div>';
     que_text.innerHTML = que_tag; //adding new span tag inside que_tag
     que_explanation.innerHTML = qs[index].explanation
      option_list.innerHTML = option_tag; //adding new div tag inside option_tag
      
     const option = option_list.querySelectorAll(".option");
     que_explanation.style.display = "none";

      // set onclick attribute to all available options
      for (i = 0; i < option.length; i++) {
          option[i].setAttribute("onclick", "optionSelected(this)");
      }
    };
  })(questions);

  

}

fetchQuestions()

