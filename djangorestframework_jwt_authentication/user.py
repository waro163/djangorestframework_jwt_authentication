
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