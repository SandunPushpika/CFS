from rest_framework.response import Response

def success_response(data, message):
    return Response({
        'data': data,
        'message': message,
        'success': True
    }, status=200)

def error_response(error):
    return Response({
        'errors': error,
        'success': False
    }, status=400)