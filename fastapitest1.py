import requests
response = requests.get("http://localhost:8000/ask", params={"question":"What's AI?"})
print(response.json())