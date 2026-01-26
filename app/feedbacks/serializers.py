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
    user_name = serializers.CharField(source="user.email", read_only=True)
    user_id = serializers.IntegerField(source="user.id", read_only=True)
    user_role = serializers.CharField(source="user.role", read_only=True)
    user_degree = serializers.CharField(source="user.degree", read_only=True)
    course_id = serializers.IntegerField(source="course.id", read_only=True)
    course_title = serializers.CharField(source="course.title", read_only=True)
    course_code = serializers.CharField(source="course.course_code", read_only=True)

    class Meta:
        model = Feedback
        fields = [
            "id",
            "user_id",
            "user_name",
            "user_role",
            "user_degree",
            "course_id",
            "course_title",
            "course_code",
            "feedback_text",
            "rating",
            "answers",
            "created_at",
        ]
