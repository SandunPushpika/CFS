from django.db.models import Avg
from app.feedbacks.models.feedback_model import Feedback
from app.feedbacks.models.question_model import Question
from app.authentication.models.user import User
from app.courses.models.course_model import Course
from django.db import transaction


class FeedbackService:
    
    @staticmethod
    @transaction.atomic
    def create_feedback(
        *,
        user_id: int,
        course_id: int,
        answers: list,
        feedback_text: str,
        rating: int
    ) -> Feedback:
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5")

        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            raise ValueError("Invalid user")

        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            raise ValueError("Invalid course")

        feedback = Feedback.objects.create(
            user=user,
            course=course,
            answers=answers,
            feedback_text=feedback_text,
            rating=rating
        )

        return feedback

    @staticmethod
    def get_all_feedbacks():
        return Feedback.objects.select_related(
            "user", "course"
        ).all()

    @staticmethod
    def get_feedbacks_by_course(course_id=None, course_code=None):
        qs = Feedback.objects.select_related("course")

        if course_id:
            qs = qs.filter(course_id=course_id)

        if course_code:
            qs = qs.filter(course__course_code=course_code)

        return qs

    @staticmethod
    def get_feedbacks_by_year(year: int):
        return Feedback.objects.filter(
            created_at__year=year
        )

    @staticmethod
    def get_feedbacks_by_semester(semester: int):
        return Feedback.objects.filter(
            course__degree_programs__contains=[
                {"semester": semester}
            ]
        )

    @staticmethod
    def get_feedbacks_by_degree_and_semester(degree_program: str, semester: int):
        return Feedback.objects.filter(
            course__degree_programs__contains=[
                {
                    "degree_program": degree_program,
                    "semester": semester
                }
            ]
        )

    @staticmethod
    def get_feedbacks_filtered(
        *,
        year: int | None = None,
        semester: int | None = None,
        degree_program: str | None = None,
        course_id: int | None = None,
        course_code: str | None = None,
    ):

        qs = Feedback.objects.select_related(
            "user", "course"
        )

        if year:
            qs = qs.filter(created_at__year=year)

        if course_id:
            qs = qs.filter(course_id=course_id)

        if course_code:
            qs = qs.filter(course__course_code=course_code)

        if semester and degree_program:
            qs = qs.filter(
                course__degree_programs__contains=[
                    {
                        "degree_program": degree_program,
                        "semester": semester
                    }
                ]
            )
        elif semester:
            qs = qs.filter(
                course__degree_programs__contains=[
                    {"semester": semester}
                ]
            )

        return qs

    @staticmethod
    def get_average_rating_by_course(
        *,
        year: int | None = None,
        semester: int | None = None,
        degree_program: str | None = None,
    ):
        qs = Feedback.objects.all()

        if year:
            qs = qs.filter(created_at__year=year)

        if semester and degree_program:
            qs = qs.filter(
                course__degree_programs__contains=[
                    {
                        "degree_program": degree_program,
                        "semester": semester
                    }
                ]
            )
        elif semester:
            qs = qs.filter(
                course__degree_programs__contains=[
                    {"semester": semester}
                ]
            )

        return (
            qs.values("course__id", "course__title", "course__course_code")
            .annotate(avg_rating=Avg("rating"))
            .order_by("-avg_rating")
        )