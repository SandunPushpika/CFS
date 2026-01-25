from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response

from app.feedbacks.services.feedback_service import FeedbackService
from app.feedbacks.serializers import (
    FeedbackCreateSerializer,
    FeedbackListSerializer,
)
from app.feedbacks.services.question_service import (
    get_all_questions,
    create_question,
    delete_question,
)
from app.utils.http_responses import success_response, error_response

@api_view(['POST', 'PUT'])
@permission_classes([AllowAny])
def feedback_crud_api(request, feedback_id=None):
    """
    POST   -> Create feedback
    PUT    -> Update feedback
    """

    if request.method == 'PUT':
        return update_feedback_api(request, feedback_id)

    serializer = FeedbackCreateSerializer(data=request.data)
    if not serializer.is_valid():
        return error_response(serializer.errors)

    try:
        feedback = FeedbackService.create_feedback(
            **serializer.validated_data
        )
    except ValueError as ex:
        return error_response(str(ex))

    response_serializer = FeedbackListSerializer(feedback)
    return success_response(
        response_serializer.data,
        "Feedback created successfully"
    )

def update_feedback_api(request, feedback_id):
    try:
        feedback = FeedbackService.update_feedback(
            feedback_id=feedback_id,
            data=request.data
        )
    except ValueError as ex:
        return error_response(str(ex))

    serializer = FeedbackListSerializer(feedback)
    return success_response(serializer.data, "Feedback updated successfully")

@api_view(['GET'])
@permission_classes([AllowAny])
def list_feedbacks_api(request):
    """
    Query params:
    - year
    - semester
    - degree_program
    - course_id
    - course_code
    """

    year = request.query_params.get("year")
    semester = request.query_params.get("semester")
    degree_program = request.query_params.get("degree_program")
    course_id = request.query_params.get("course_id")
    course_code = request.query_params.get("course_code")

    feedbacks = FeedbackService.get_feedbacks_filtered(
        year=int(year) if year else None,
        semester=int(semester) if semester else None,
        degree_program=degree_program,
        course_id=int(course_id) if course_id else None,
        course_code=course_code,
    )

    serializer = FeedbackListSerializer(feedbacks, many=True)
    return success_response(serializer.data, "")


@api_view(['GET'])
@permission_classes([AllowAny])
def feedback_stats_api(request):
    """
    Query params:
    - year
    - semester
    - degree_program
    """

    year = request.query_params.get("year")
    semester = request.query_params.get("semester")
    degree_program = request.query_params.get("degree_program")

    data = FeedbackService.get_average_rating_by_course(
        year=int(year) if year else None,
        semester=int(semester) if semester else None,
        degree_program=degree_program,
    )

    return success_response(data, "")

@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def question_api(request):
    """
    GET  -> List all questions
    POST -> Create a question
    """

    if request.method == 'GET':
        questions = get_all_questions()
        data = [
            {
                "id": q.id,
                "text": q.text,
            }
            for q in questions
        ]
        return success_response(data, "")

    text = request.data.get("text")

    if not text:
        return error_response("Question text is required")

    try:
        question = create_question(text=text)
    except Exception as ex:
        return error_response(str(ex))

    return success_response(
        {
            "id": question.id,
            "text": question.text,
        },
        "Question created successfully"
    )

@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_question_api(request, question_id):
    """
    DELETE -> Delete question
    """

    try:
        delete_question(question_id)
    except ValueError as ex:
        return error_response(str(ex))

    return success_response(
        None,
        "Question deleted successfully"
    )