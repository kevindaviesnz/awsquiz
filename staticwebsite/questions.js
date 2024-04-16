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
  
  const response = await fetch("https://5t3emk4n5f.execute-api.ap-southeast-2.amazonaws.com/asq/awsquiz");
  const json = await response.json();
  console.log(json["questions"]);
  
  // Map questions to get the expected format
  questions = json["questions"].map((question_set, i) => {
    return {
      "numb": i + 1,
      "question": question_set["question"],
      "options": question_set["answers"],
      "answer": question_set["correct_answer"]
    }
  })

  // Here we create a closure, call it immediately, and return it as a function.
  showQuestionSet = ((qs) => {
   return (index) => {
     // Was showQuetions(index)
      const que_text = document.querySelector(".que_text");
      //creating a new span and div tag for question and option and passing the value using array index
      let que_tag = '<span>' + qs[index].numb + ". " + qs[index].question + '</span>';
      let option_tag = '<div class="option"><span>' + qs[index].options[0] + '</span></div>'
          + '<div class="option"><span>' + qs[index].options[1] + '</span></div>'
          + '<div class="option"><span>' + qs[index].options[2] + '</span></div>'
          + '<div class="option"><span>' + qs[index].options[3] + '</span></div>';
      que_text.innerHTML = que_tag; //adding new span tag inside que_tag
      option_list.innerHTML = option_tag; //adding new div tag inside option_tag
      
      const option = option_list.querySelectorAll(".option");

      // set onclick attribute to all available options
      for (i = 0; i < option.length; i++) {
          option[i].setAttribute("onclick", "optionSelected(this)");
      }
    };
  })(questions);

  

}

fetchQuestions()

