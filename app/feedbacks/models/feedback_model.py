import django.db.models as models
from app.authentication.models.user import User
from app.courses.models.course_model import Course
from . import question_model

"""
answers: [
    {
        "question_id": 1,
        "question_text": "How would you rate the course content?",
        "rating": 5
    }
]
"""

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    answers = models.JSONField(null=True)
    feedback_text = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'feedbacks'