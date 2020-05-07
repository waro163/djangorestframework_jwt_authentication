
class BaseUser:
    def __init__(self,**kwargs):
        user_id = getattr(self,'id',None) or kwargs.get('id')
        if user_id:
            self.id = self.pk = user_id
        else:
            raise Exception("please package user id in jwt authorization token, format is {id:'xxxx'}")

    @property
    def is_authenticated(self):
        return True

class User(BaseUser):
    def __init__(self,payload):
        if not isinstance(payload,dict):
            raise
        for key, value in payload.items():
            setattr(self, key, value)
        super().__init__()

class RemoteUser(object):

    # This property is for drf RemoteUser authenticate
    @property
    def is_active(self):
        return True

    def authenticate(self, request, **kwargs):
        remote_user_msg = kwargs.get('remote_user')
        if remote_user_msg:
            for key, value in remote_user_msg.items():
                setattr(self, key, value)
            return self
        return None

    # This property is for drf check permission
    @property
    def is_authenticated(self):
        return True