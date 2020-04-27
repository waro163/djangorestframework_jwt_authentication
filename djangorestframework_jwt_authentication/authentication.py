from django.utils.module_loading import import_string
from django_jwt_middleware.utils.get_settings_value import get_setting_value
from rest_framework.authentication import BaseAuthentication

class JwtAuthentication(BaseAuthentication):
    def authenticate(self, request):
        jwt_payload = request.META['jwt_payload']
        if jwt_payload:
            try:
                rest_framework_jwt_user = get_setting_value('REST_FRAMEWORK_JWT_USER')
                user_class_path = rest_framework_jwt_user.get('USER_CLASS_PATH')
                user_class = import_string(user_class_path)
                user = user_class(jwt_payload)
            except Exception as e:
                return None
            return user,jwt_payload
        return None

    def authenticate_header(self, request):
        return "Token"