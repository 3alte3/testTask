import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testTask.settings')
app = Celery('testTask')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
app.conf.enable_utc = False

app.conf.update(timezone='Europe/Minsk')

app.conf.beat_schedule = {
    'send_mail': {
        'task': 'statistic.tasks.test_func',
        'schedule': 30.0,
    }
}


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
