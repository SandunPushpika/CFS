from rest_framework.views import exception_handler
from app.utils.http_responses import error_response

def custom_exception_handler(exc, context):
    return error_response(exc.__str__())