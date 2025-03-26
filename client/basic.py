import requests

endpoint = "http://127.0.0.1:8000/api/plants/"

headers = {
    "Authorization" : "Token f113ba35a3c2d555cc4f719878e6f2b3617ae929"
}

response = requests.get(endpoint, headers=headers)

print(response.json())