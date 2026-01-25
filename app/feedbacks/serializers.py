from rest_framework import serializers
from app.feedbacks.models.feedback_model import Feedback
from app.feedbacks.models.question_model import Question


class FeedbackCreateSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    course_id = serializers.IntegerField()
    answers = serializers.JSONField()
    feedback_text = serializers.CharField()
    rating = serializers.IntegerField(min_value=1, max_value=5)


class FeedbackListSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source="user.username", read_only=True)
    course_title = serializers.CharField(source="course.title", read_only=True)
    course_code = serializers.CharField(source="course.course_code", read_only=True)

    class Meta:
        model = Feedback
        fields = [
            "id",
            "user_name",
            "course_title",
            "course_code",
            "feedback_text",
            "rating",
            "answers",
            "created_at",
        ]
