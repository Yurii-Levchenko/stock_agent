import os
from celery import Celery

# Set default settings module for Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stock_agent.settings')

app = Celery('stock_agent')

# Load task modules from all registered Django app configs
app.config_from_object('django.conf:settings', namespace='CELERY')

# Autodiscover tasks in all Django apps
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

# broker_connection_retry_on_startup = True