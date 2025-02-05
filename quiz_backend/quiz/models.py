from django.db import models

# Create your models here.


class Question(models.Model):
    LEVELS = [(1, "Current"), (2, "Recent"), (3, "Legend")]
    question_text = models.CharField(max_length=255)
    options = models.JSONField()
    correct_answer = models.CharField(max_length=255)
    level = models.IntegerField(choices=LEVELS)

    def __str__(self):
        return self.question_text
