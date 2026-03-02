import json

response_text = '{"status": "success", "errors": 5}'

data = json.loads(response_text)

print(data["status"])
print(data["errors"])