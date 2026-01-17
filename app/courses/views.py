from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from app.utils.permisions import IsAdmin
from .serializers import CourseSerializer
from app.utils.http_responses import success_response, error_response

from app.courses.services.course_service import get_all_courses, get_courses_by_degree_and_semester, update_course, delete_course

@api_view(['POST', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def create_course(request, course_id=None):
    if(request.method == 'PUT'):
        return update_course_api(request)
    
    if(request.method == 'DELETE'):
        return delete_course_api(course_id)

    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return success_response(serializer.data, "Course created successfully")
    return error_response("Course alreay exists!")

@api_view(['GET'])
@permission_classes([AllowAny])
def list_all_courses(request):
    courses = get_all_courses()
    serializer = CourseSerializer(courses, many=True)
    return success_response(serializer.data, "")

@api_view(['GET'])
@permission_classes([AllowAny])
def get_course_by_degree(request):
    degree = request.query_params.get('degree_program', None)
    semester = request.query_params.get('semester', 1)
    print(degree, semester)
    if not degree or not semester:
        return error_response("degree_program and semester query parameters are required")
    courses = get_courses_by_degree_and_semester(degree_program=degree, semester=semester)
    serializer = CourseSerializer(courses, many=True)
    return success_response(serializer.data, "")

def update_course_api(request):
    print("Updating course...")
    course_id = request.data.get('id')
    name = request.data.get('title')
    course_code = request.data.get('course_code')
    degree_programs = request.data.get('degree_programs')
    try:
        updated_course = update_course(
        course_id=course_id,
        name=name,
        course_code=course_code,
        degree_programs=degree_programs
        )
        updated_serializer = CourseSerializer(updated_course)
        return success_response(updated_serializer.data, "Course updated successfully")
    except ValueError as e:
        return error_response(str(e))

def delete_course_api(course_id):
    delete_course(course_id)
    return success_response(None, "Course deleted successfully")