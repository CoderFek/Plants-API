import requests


endpoint = 'http://127.0.0.1:8000/api/users/me/'

headers = {
    "Authorization": "Bearer eyJhbBciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ0Nzg3ODc1LCJpYXQiOjE3NDQ3ODc1NzUsImp0aSI6IjIyOTIzNjQwZDJmNjQyNmI5ZWM1MWMyMDFjOGI4OTIyIiwidXNlcl9pZCI6MX0.fXTtviTAlHlxMXML0kgbfUx9_53aRvhcBTKyUefFagA"
}

response = requests.get(endpoint, headers=headers)

print(response.json())