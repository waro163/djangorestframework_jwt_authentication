
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
        remote_user_msg = kwargs.get('remote_user')
        if remote_user_msg:
            for key, value in remote_user_msg:
                setattr(self, key, value)
            return self
        return None

    # This property is for drf check permission
    @property
    def is_authenticated(self):
        return True