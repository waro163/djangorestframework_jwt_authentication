
you must configure REST_FRAMEWORK_JWT_USER in the settings.py

REST_FRAMEWORK_JWT_USER = {
    "USER_CLASS_PATH": "djangorestframework_jwt_authentication.user.User",
}

REST_FRAMEWORK = {
    ...
    'DEFAULT_AUTHENTICATION_CLASSES': (
         'djangorestframework_jwt_authentication.authentication.JwtAuthentication',
         'rest_framework.authentication.SessionAuthentication',
    ),
}