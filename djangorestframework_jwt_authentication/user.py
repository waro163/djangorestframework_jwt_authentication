
class BaseUser:
    def __init__(self,user_id):
        self.id = user_id

    @property
    def is_authenticated(self):
        return True

class User(BaseUser):
    def __init__(self,payload):
        if not isinstance(payload,dict):
            raise
        for key, value in payload.items():
            setattr(self, key, value)

class RemoteUser(object):

    # This property is for drf RemoteUser authenticate
    @property
    def is_active(self):
        return True

    def authenticate(self, request, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        return self

    # This property is for drf check permission
    @property
    def is_authenticated(self):
        return True