from rest_framework import serializers
from app.courses.models.course_model import Course
from app.courses.services.course_service import create_course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'course_code',
            'degree_programs',
        )
    def create(self, validated_data):
        return create_course(
            name=validated_data.get('title'),
            course_code=validated_data.get('course_code'),
            degree_programs=validated_data.get('degree_programs')
        )