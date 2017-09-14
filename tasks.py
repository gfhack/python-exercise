import requests
import json

from celery import Celery

app = Celery('tasks', backend='redis://localhost', broker='redis://localhost')

@app.task
def add(x, y):
    return x + y

@app.task
def users():
    url = 'http://localhost:3000/users/1'
    req = requests.get(url)
    return json.loads(req.text)