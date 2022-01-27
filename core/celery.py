import os
from celery.schedules import crontab
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule = {
    "annul_upvote": {
        "task": "app.posts.tasks.annul_upvote",
        "schedule": crontab(minute=0, hour=0),

# minute=0, hour=0
    }
}