from asgiref.sync import sync_to_async

from backend.models import UserModel


@sync_to_async
def add_user(user_id, name):
    try:
        user = UserModel(user_id=user_id, name=name, user_type="USER").save()
        return user
    except Exception as err:
        print(err)
        return None


@sync_to_async
def get_user(user_id):
    try:
        user = UserModel.objects.get(user_id=user_id)
        return user
    except:
        return None