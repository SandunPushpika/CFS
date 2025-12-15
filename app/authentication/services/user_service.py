from app.authentication.models import User
from rest_framework_simplejwt.tokens import RefreshToken

def create_user(data):
    if User.objects.filter(email=data['email']).exists():
        raise ValueError("Email is already in use")
    
    user = User(**data)
    user.set_password(data['password'])
    user.save()
    return user

def authenticate_user(email, password):
    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return None

    if not user.check_password(password):
        return None
    
    if not user.is_active:
        return None

    refresh = RefreshToken.for_user(user)
    return {
        'role': user.role,
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }