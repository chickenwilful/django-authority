from django.conf import settings


def get_user_class():
    return settings.AUTH_USER_MODEL
    # return auth.get_user_model()
    # if hasattr(auth, "get_user_model"):
    #     return auth.get_user_model()
    # else:
    #     return auth.models.User


User = get_user_class()