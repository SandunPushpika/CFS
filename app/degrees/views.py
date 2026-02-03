from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from app.degrees.serializers import DegreeSerializer
from app.utils.http_responses import success_response, error_response

from app.degrees.services.degree_service import (
    get_all_degrees,
    delete_degree,
)


@api_view(['POST', 'DELETE'])
@permission_classes([AllowAny])
def create_degree_api(request, degree_id=None):
    if request.method == 'DELETE':
        return delete_degree_api(degree_id)

    serializer = DegreeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return success_response(serializer.data, "Degree created successfully")
    return error_response(serializer.errors)


@api_view(['GET'])
@permission_classes([AllowAny])
def list_all_degrees(request):
    degrees = get_all_degrees()
    serializer = DegreeSerializer(degrees, many=True)
    return success_response(serializer.data, "")


def delete_degree_api(degree_id):
    try:
        delete_degree(degree_id)
    except ValueError as ex:
        return error_response(str(ex))

    return success_response(None, "Degree deleted successfully")
