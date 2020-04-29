Before you user this module, you must install [django_jwt_middleware](https://github.com/waro163/django_jwt_middleware.git)

# JwtUser
if you use JwtAuthentication in drf,
you must configure following configuration in the settings.py

REST_FRAMEWORK_JWT_USER = {
    "USER_CLASS_PATH": "djangorestframework_jwt_authentication.user.User",
}

REST_FRAMEWORK = {
    ...
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'djangorestframework_jwt_authentication.authentication.JwtAuthentication',
        ...
    ),
}

# RemoteUser
if you use RemoteUserAuthentication in drf,
you must configure following configuration in the settings.py

AUTHENTICATION_BACKENDS = [
    'djangorestframework_jwt_authentication.user.RemoteUser',
]

REST_FRAMEWORK = {
    ...
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.RemoteUserAuthentication',
        ...
    ),
}