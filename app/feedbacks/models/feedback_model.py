import django.db.models as models
from app.authentication.models.user import User
from app.courses.models.course_model import Course
from . import question_model

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    question = models.ForeignKey(question_model.Question, on_delete=models.CASCADE)
    feedback_text = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'feedbacks'