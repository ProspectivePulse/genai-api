import requests

payload = {"query": "Tell me a joke"}
response = requests.post("http://localhost:8000/ask", json=payload)
print(response.json())