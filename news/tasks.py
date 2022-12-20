from config.celery import app
from config.helpers import send_sms_code, validate_sms_code
# from .models import Notification
from account.models import UserModel
from .send_notification import sendPush


@app.task
def send_notification_func(title, description, image, type, foreign_id):
    # notification = Notification.objects.get(id=pk)
    # title = notification.title
    # description = notification.description
    # image = notification.image
    # notification_name = notification.notification_name

    # sending to firebase
    try:
        image_path = image.path
    except:
        image_path = None

    keys = list(UserModel.objects.filter().values_list('notificationKey', flat=True))
    res = []
    for val in keys:
        if val != None :
            res.append(val)

    print(res)
    res = sendPush(title=title, description=description, registration_tokens=res,
                    image=image_path, notification_name=type, dataObject={'id': foreign_id})

