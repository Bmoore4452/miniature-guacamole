from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Question
import random
import openai


@api_view(["GET"])
def get_questions(request, level):
    questions = list(Question.objects.filter(level=level))
    random.shuffle(questions)
    return Response(
        [{"question": q.question_text, "options": q.options} for q in questions[:5]]
    )


@api_view(["POST"])
def submit_answers(request):
    user_answers = request.data.get("answers", {})
    correct_count = sum(
        1
        for qid, answer in user_answers.items()
        if Question.objects.get(id=qid).correct_answer == answer
    )
    return Response({"score": (correct_count / len(user_answers)) * 100})


@api_view(["POST"])
def get_feedback(request):
    user_score = request.data.get("score")
    prompt = f"The user scored {user_score}% in a nursing quiz. Provide personalized feedback."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}]
    )
    return Response({"feedback": response["choices"][0]["message"]["content"]})
