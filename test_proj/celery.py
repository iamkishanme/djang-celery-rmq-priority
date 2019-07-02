import os
from celery import Celery
from kombu import Queue

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_proj.settings')

app = Celery('test_proj', broker='amqp://kishan:pass1234@localhost:5672/test_host')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.task_queues = (
    Queue('task_one_q', queue_arguments={'x-max-priority': 10}),
    Queue('task_two_q', queue_arguments={'x-max-priority': 10}),
)

app.autodiscover_tasks()

app.conf.task_default_queue = 'default'
app.conf.task_default_exchange = 'default'
app.conf.task_default_routing_key = 'default'

# rabbitmqadmin --vhost=test_host --username=kishan --password='pass1234' -f tsv -q list queues name | while read queue; do rabbitmqadmin --vhost=test_host --username=kishan --password='pass1234' -q delete queue name=${queue}; done
