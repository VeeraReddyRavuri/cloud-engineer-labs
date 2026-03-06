import requests

def requestsPosting(url, payload, headers):
    try: 
        response = requests.post(
            url,
            json = payload,
            headers = headers,
            timeout = 4
        )
        print(response.status_code)
    except requests.exceptions.Timeout:
        print("Request timed out")


url = input("Enter Url: ")

headers = {
    "Authorization": "Bearer test-token"
}

payload = {
    "message": "Disk usage is at 85% which is above threshold"
}

requestsPosting(url, headers, payload)

