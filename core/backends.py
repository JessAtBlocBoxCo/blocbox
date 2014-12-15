from django.contrib.auth.backends import ModelBackend
#from django.contrib.admin.models import User
from core.models import UserInfo

class EmailAuthBackEnd(ModelBackend):
    def authenticate(self, email=None, password=None, **kwargs):
        try:
            user = UserInfo.objects.get(email=email)

            if user.check_password(password):
                return user
            return None
        except UserInfo.DoesNotExist:
            return None
