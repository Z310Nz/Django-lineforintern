# backends.py
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class LineAuthenticationBackend(ModelBackend):
    def authenticate(self, request, line_user_id=None, **kwargs):
        User = get_user_model()

        # Check if the user with the given Line user_id exists
        try:
            user = User.objects.get(line_user_id=line_user_id)
        except User.DoesNotExist:
            # If the user doesn't exist, you might want to create a new user here
            return None

        return user

    def get_user(self, user_id):
        User = get_user_model()

        # Retrieve the user by ID
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
