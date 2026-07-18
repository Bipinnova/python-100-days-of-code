from data import question_data
import random


def get_questions():
    quiz_questions = []

    for question in question_data:
        safe_question = {}

        safe_question["id"] = question["id"]
        safe_question["question"] = question["question"]

        safe_question["options"] = []

        safe_question["options"].append(question["correct_answer"])
        safe_question["options"].append(
            "False"
            if question["correct_answer"] == "True"
            else "True"
        )

        random.shuffle(safe_question["options"])

        quiz_questions.append(safe_question)

    return quiz_questions


def check_answer(request):
    for question in question_data:
        if question["id"] == request.question_id:

            is_correct = (
                question["correct_answer"] == request.selected_answer
            )

            return {
                "question_id": request.question_id,
                "selected_answer": request.selected_answer,
                "correct_answer": question["correct_answer"],
                "correct": is_correct,
                "message": (
                    "Correct Answer! 🎉"
                    if is_correct
                    else "Wrong Answer! ❌"
                )
            }

    return {
        "message": "Question not found.",
        "correct": False
    }