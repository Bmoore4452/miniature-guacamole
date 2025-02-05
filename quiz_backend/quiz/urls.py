from django.urls import path
from .views import get_questions, submit_answers, get_feedback

urlpatterns = [
    path("questions/<int:level>/", get_questions),
    path("submit/", submit_answers),
    path("feedback/", get_feedback),
]
