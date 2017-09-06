import requests
import json

url = 'http://jsonplaceholder.typicode.com/posts/2'

req = requests.get(url)

data = json.loads(req.text)

print req.status_code
print data

payload = {'title': 'some title', 'body': 'some text', 'userId': 1}

post_url = 'http://jsonplaceholder.typicode.com/posts'

req = requests.post(post_url, json=payload)

print req.status_code
print req.text
