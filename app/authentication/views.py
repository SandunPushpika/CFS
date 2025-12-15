from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import RegisterSerializer
from .services.user_service import authenticate_user
from app.utils.http_responses import success_response, error_response
from app.utils.permisions import IsAdmin

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)

    if(serializer.is_valid()):
        serializer.save()
        return success_response(None, "User registration successfull")
    return error_response(serializer.errors)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    email = request.data.get('email')
    password = request.data.get('password')

    tokens = authenticate_user(email, password)
    if tokens is None:
        return error_response("Invalid credentials or inactive account")

    return success_response(tokens, "Login successful")

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_view(request):
    return success_response(None, "You have accessed a protected view")

@api_view(['GET'])
@permission_classes([IsAdmin])
def another_protected_view(request):
    return success_response(None, "You have accessed another protected view")