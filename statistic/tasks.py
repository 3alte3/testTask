import requests
from celery import shared_task
from django.core.mail import send_mail
from testTask import settings
from a import create_message
from registration.models import NewUser
from rest_framework.authtoken.models import Token


@shared_task(bind=True)
def test_func(self):
    for user in NewUser.objects.all():
        print(user)
        mail_subject = "Hi! Your statistic"
        message = create_message(user.id)
        to_email = user.email
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[to_email],
            fail_silently=True,
        )
    return 'Done'


def create_message(pk) -> str:
    try:
        token = Token.objects.get(user_id=pk)
    except BaseException:
        return 'No statistic'
    if token:
        headers = {'Authorization': f'Token {token.key}'}
        return requests.get('http://127.0.0.1:8000/stat/', headers=headers).json()
    else:
        return 'No statistic'
