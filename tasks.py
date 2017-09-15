import requests
import json

from requests.exceptions import RequestException

from celery import Celery

app = Celery('tasks', backend='redis://localhost', broker='librabbitmq://localhost')

@app.task
def add(x, y):
    return x + y


@app.task(default_retry_delay=5, autoretry_for=(RequestException,), retry_backoff=True, max_retries=None)
def users():
    url = 'http://localhost:3000/users/1'
    req = requests.get(url)
    return json.loads(req.text)
