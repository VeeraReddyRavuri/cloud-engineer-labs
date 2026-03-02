import json

with open("config.json", "r") as f:
    config = json.load(f)

print(config["project"])
print(config["database"])
print(config["alerts"])