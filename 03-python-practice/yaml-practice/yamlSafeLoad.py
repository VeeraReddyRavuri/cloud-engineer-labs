import yaml

with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

error_rate = config.get("thresholds", {}).get("alerts", {}).get("error_rate") #using .get to validate missing keys

# try/except way to validate missing keys
try:
    github = config["webhooks"]["github"]
    print(github)
except KeyError:
    print("Github webhook not configured, Skipping")

#print required values from config.yaml
print(error_rate)
print(config["project"])
print(config["database"])
print(config["thresholds"]["restart"]["max_attempts"]) #nested dictionaries